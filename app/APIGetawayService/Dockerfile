FROM python:3.10-slim

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install kafka-python

COPY . /opt/app

ENTRYPOINT ["python", "/opt/app/main.py"]

