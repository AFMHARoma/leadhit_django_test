FROM python:3.10-slim-buster
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY docker-requirements.txt .
RUN pip install -r docker-requirements.txt

COPY . /app
