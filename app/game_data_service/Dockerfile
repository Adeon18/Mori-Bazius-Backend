FROM python:3.10.5-slim-buster

COPY common/ /common/

WORKDIR /app

COPY game_data_service/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY game_data_service/ .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0" ]