# Dockerfile for backend

FROM python:3.12.5-alpine3.19

WORKDIR /app

RUN apk update && \
	apk add --virtual python-dev && \
	apk add --virtual build-deps gcc musl-dev && \
	apk add postgresql-dev && \
	apk add tzdata

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000