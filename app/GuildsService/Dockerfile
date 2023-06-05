FROM python:3.10-slim

WORKDIR /usr/src/guilds
COPY . .
RUN pip install -r requirements.txt

CMD python -m controller.guilds_controller
