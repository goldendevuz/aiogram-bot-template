FROM python:3.12-slim

WORKDIR /usr/src/app/bot

COPY requirements.txt /usr/src/app/bot

RUN pip install --upgrade pip setuptools wheel

RUN pip install -r /usr/src/app/bot/requirements.txt

COPY . /usr/src/app/bot
