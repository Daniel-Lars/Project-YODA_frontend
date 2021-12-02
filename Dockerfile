FROM python:3.8.12-buster

COPY frontend /frontend
COPY requirements.txt /requirements.txt
COPY yoda.png /yoda.png
RUN pip install -r requirements.txt
CMD streamlit run --server.port 8080 --server.enableCORS=false frontend/app.py
