FROM python:3.11.3-slim-buster

WORKDIR /app

COPY SnapshotService/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY SnapshotService/ .

CMD [ "python", "/app/main.py" ]