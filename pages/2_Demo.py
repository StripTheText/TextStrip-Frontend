# Imports for the Streamlit app
import streamlit as st
import pyperclip
import PyPDF2
import docx
from audiorecorder import audiorecorder
from io import BytesIO

# Import of internal libraries
from functions.help_env import find_env_file, load_env_file
from functions.S2C_Communication import build_url_rest_api, send_request_rest_api


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
            pass

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
                        type=['txt', 'pdf', 'docx'],
                        accept_multiple_files=False,
                        label_visibility="hidden"
                    )
                    if file_in is not None:
                        val: str = ""
                        if file_in.type == "text/plain":
                            val = file_in.read().decode('utf-8')
                        elif file_in.type == "application/pdf":
                            pass
                            # TODO: Implement the function to read pdf Files
                        elif file_in.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                            with file_in as f:
                                doc = docx.Document(BytesIO(f.read()))
                                for para in doc.paragraphs:
                                    val += para.text
                            # TODO: Implement the function to read docx Files
                        elif file_in.type == "audio/mpeg":
                            pass
                            # TODO: Implement the function Audio Request to Backend
                        text_input_value_bool = True
                        text_input_value = val

                elif input_type == 'Microphone':
                    audio = audiorecorder("Click to record", "Recording...")
                    if len(audio) > 0:
                        st.audio(audio.tobytes())
                        text_input_value_bool = True
                        # TODO: Implement the function Audio Request to Backend

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
            value="",
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
        txt_summ = st.text_area('Summary of the text', key="text_output_field_key", height=500)

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
            # TODO: Add functionality to the button

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
            st.button(
                label="Copy to Clipboard",
                key="copy_clipboard",
                use_container_width=True,
                on_click=pyperclip.copy(text=txt_summ)
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
    st.session_state["class_output_field_key"] = ""
    st.session_state["text_output_field_key"] = ""


demo_site()
