FROM python:3.10-slim

RUN apt-get update

RUN pip install --upgrade pip

COPY common/ /opt/common/

WORKDIR /opt/app

RUN pip install uvicorn
RUN pip install fastapi
RUN pip install kafka-python
RUN pip install requests 

COPY APIGetawayService/ .

ENTRYPOINT ["python", "/opt/app/main.py"]
