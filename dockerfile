FROM python:3.11.2-alpine3.17

WORKDIR /usr/src
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 8000
