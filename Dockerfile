FROM python

RUN apt-get update

RUN mkdir models src temp

COPY requirements.txt .

COPY src/ src/

RUN pip install -r requirements.txt

RUN python src/server.py