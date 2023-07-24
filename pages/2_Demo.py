# Imports for the Streamlit app
import asyncio
import json

import streamlit as st
import pyperclip
import PyPDF2
import docx
from audiorecorder import audiorecorder
from io import BytesIO
import tempfile
import os
import pathlib
import whisper
import requests


# Definition of the Layout of the Streamlit app
def demo_site():
    """
    Input column for the app (Text, Text Area, File Upload, Microphone, Text Compression Rate, etc.)
    """
    # Configuration of the Streamlit site
    st.set_page_config(
        layout="wide",
        page_title="Strip the Text - Demo",
        page_icon="🧊",
        initial_sidebar_state="collapsed")

    # Definition of Constants
    text_input_value_bool: bool = False
    text_input_value: str = ""

    # Defition Session State
    if 'class' not in st.session_state:
        st.session_state['class'] = ""

    if 'summary' not in st.session_state:
        st.session_state['summary'] = ""

    if 'real_compression_rate' not in st.session_state:
        st.session_state['real_compression_rate'] = 0.0

    # 1. Row: Title
    row_1_container = st.container()
    with row_1_container:
        st.title("Strip the Text - Demo")

    # 2. Row
    row_2_container = st.container()
    with row_2_container:
        st.header("Parameter of the Demo")
        row_2_col_1, row_2_col_2 = st.columns([0.3, 0.7], gap="large")
        with row_2_col_1:
            # Slider for the text compression rate
            text_compression_rate = st.slider("Text Compression Rate", .3, 1.0, .5, .1)

        with row_2_col_2:
            row_2_col_2_1, row_2_col_2_2 = st.columns(2, gap="small")

            with row_2_col_2_1:
                input_type = st.radio(
                    "Input Type",
                    ('Text Area', 'File Upload', 'Microphone'),
                    horizontal=True
                )
            with row_2_col_2_2:
                if input_type == 'Text Area':
                    text_input_value_bool = True

                elif input_type == 'File Upload':
                    file_in = st.file_uploader(
                        'Upload a file',
                        type=['txt', 'docx'],
                        accept_multiple_files=False,
                        label_visibility="hidden"
                    )
                    if file_in is not None:
                        val: str = ""
                        if file_in.type == "text/plain":
                            val = file_in.read().decode('utf-8')
                        elif file_in.type == "application/pdf":
                            pass
                        elif file_in.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                            with file_in as f:
                                doc = docx.Document(BytesIO(f.read()))
                                for para in doc.paragraphs:
                                    val += para.text
                        elif file_in.type == "audio/mpeg":
                            pass
                        text_input_value_bool = True
                        text_input_value = val

                elif input_type == 'Microphone':
                    audio = audiorecorder("Click to record", "Recording...")
                    if len(audio) > 0:
                        st.audio(audio.tobytes())
                        text_input_value_bool = True
                        text_input_value = audio2text(audio)

    # 3. Row: Input & Output Column
    row_3_col_1, row_3_col_2 = st.columns(2)

    # 3.1. Row: Input Column (Text-Label)
    with row_3_col_1:
        st.header("Input for the App")

    # 3.2. Row: Output Column (Classification)
    with row_3_col_2:
        st.header("Output of the App")
        txt_class = st.text_input(
            'Classification of the text',
            key="class_output_field_key",
            value=st.session_state['class'],
            disabled=True
        )

    # 4. Row: Input & Output Column (Text-Fields)
    row_4_col_1, row_4_col_2 = st.columns(2)

    # 4.1. Row: Input Column (Text-Field)
    with row_4_col_1:
        if text_input_value_bool:
            text_input_value = st.text_area('Original Text', key="text_input_value_field", height=500,
                                            value=text_input_value)

    # 4.2. Row: Output Column (Text-Field)
    with row_4_col_2:
        txt_summ = st.text_area('Summary of the text', key="text_output_field_key", height=500,
                                value=st.session_state['summary'])

    # 5. Row: Control Buttons
    row_5_col_1, row_5_col_2 = st.columns(2)

    # 5.1. Row: Control Buttons (Under Input Column)
    with row_5_col_1:
        col_5_1, col_5_2, col_5_3 = st.columns(3)

        # 5.1.1: Select Operation Mode
        with col_5_1:
            operation = st.selectbox(
                label="Which operation should be run?",
                options=("Text Classification", "Text Summarization", "Text Classification & Summarization"),
                key="operation",
                label_visibility="collapsed",
            )

        # 5.1.2: Start Classification or Summarization
        with col_5_2:
            go_action = st.button(
                label="Go!",
                key="action",
                use_container_width=True,
            )
            if go_action:
                result_class, result_summ = None, None
                if operation == "Text Classification":
                    result_class = asyncio.run(classify_text(text_input_value))
                elif operation == "Text Summarization":
                    result_summ = asyncio.run(summarize_text(text_compression_rate, text_input_value))
                elif operation == "Text Classification & Summarization":
                    result_class = asyncio.run(classify_text(text_input_value))
                    result_summ = asyncio.run(summarize_text(text_compression_rate, text_input_value))
                if result_class is not None:
                    if result_class.status_code == 200:
                        data = result_class.json()
                        st.session_state['class'] = data['outputClass']
                        st.experimental_rerun()
                if result_summ is not None:
                    if result_summ.status_code == 200:
                        data = result_summ.json()
                        st.session_state['summary'] = data['summary']
                        st.session_state['real_compression_rate'] = data['real_compression_rate']
                        st.experimental_rerun()
        # 5.1.3: Clear Input
        with col_5_3:
            st.button(
                label="Clear Input",
                key="clear_in",
                use_container_width=True,
                on_click=clear_input
            )

    # 5.2. Row: Control Buttons (Under Output Column)
    with row_5_col_2:
        col_5_a, col_5_b, col_5_c = st.columns(3)

        # 5.2.1: Copy Output
        with col_5_a:
            # st.button(
            #    label="Copy to Clipboard",
            #    key="copy_clipboard",
            #    use_container_width=True,
            #    on_click=pyperclip.copy(text=txt_summ)
            # )
            real_compression_rate = st.text_input(
                'Real Compression Rate',
                key="real_compression_rate_txt",
                value=st.session_state['real_compression_rate'],
                disabled=True
            )

        # 5.2.2: Clear Input and Output
        with col_5_b:
            st.button(
                label="Clear Input and Output Field",
                key="clear_in_out",
                use_container_width=True,
                on_click=clear_all
            )

        # 5.2.3: Download Output
        with col_5_c:
            st.download_button(
                label="Download Result as .txt",
                data=txt_summ,
                mime="text/plain",
                file_name="result.txt",
                use_container_width=True
            )


# Helper Function for the Demo
def clear_input():
    st.session_state["text_input_value_field"] = ""


def clear_all():
    st.session_state["text_input_value_field"] = ""
    st.session_state["class"] = ""
    st.session_state["summary"] = ""


# Define the function to convert audio to text
@st.cache_data
def audio2text(
        audio2transcript: audiorecorder = None) -> str:
    """
    Function to convert audio to text using the Open AI-Whisper Model
    :param audio2transcript: Audio which needs to be transcribed
    :return: str: Transcribed text
    """
    # Download the Open AI-Whisper Model
    whisper_model = whisper.load_model(
        name="base.en",
        download_root=str(pathlib.Path.joinpath(pathlib.Path.cwd(), "models", "whisper")),
        in_memory=False
    )
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
        fp.write(audio2transcript.tobytes())
        temp_filename = fp.name

    result = whisper_model.transcribe(audio=temp_filename)

    os.remove(temp_filename)

    # Return the result of the transcription
    if result["text"] is not None:
        return result["text"]
    else:
        return "Warning: No text found in the audio file!"


async def classify_text(input_text: str):
    return requests.post(url="http://localhost:8080/api/classifier/",
                         data=json.dumps({"text": input_text}))


async def summarize_text(compression_rate: float, input_text: str):
    if compression_rate <= 0.3:
        return requests.post(url="http://localhost:8080/api/summarizer/",
                             data=json.dumps({"compression_rate": compression_rate, "text": input_text}))
    else:
        return requests.post(url="http://localhost:8080/api/summarizer/compress",
                             data=json.dumps({"compression_rate": compression_rate, "text": input_text}))


demo_site()
