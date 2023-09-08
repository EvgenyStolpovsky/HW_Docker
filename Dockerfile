FROM python:3.11-slim-buster

WORKDIR /HW_Django_DRF


COPY ./requirements.txt /HW_Django_DRF/

RUN pip install -r requirements.txt

COPY . .
