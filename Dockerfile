# Dockerfile für Streamlit-App
# Ziehen des Basisimages von Docker Hub
FROM python:3.11-slim

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Installieren Sie ffmpeg
RUN apt-get update --fix-missing && apt-get install -y ffmpeg

# Kopieren Sie den Projektcode in den Container
COPY . .

# Installieren Sie die benötigten Python-Pakete
RUN pip install -r requirements.txt

# Exponieren Sie den Port, auf dem Streamlit läuft
EXPOSE 8501

# Führen Sie Streamlit aus, wenn der Container gestartet wird
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Wie soll der Container gestartet werden?
ENTRYPOINT ["streamlit", "run", "Introduction.py", "--server.port=8501", "--server.address=0.0.0.0"]

