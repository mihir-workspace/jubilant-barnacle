FROM python:3.9.9-slim-buster

RUN apt-get update

RUN apt-get install git -y

RUN mkdir models src temp

COPY requirements.txt .

COPY src/ src/

RUN pip install -r requirements.txt

WORKDIR /src/

ENTRYPOINT python server.py
