# docker/backend/Dockerfile

FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
	apk add --virtual python-dev && \
	apk add --virtual build-deps gcc musl-dev && \
	apk add postgresql-dev && \
	apk add tzdata
RUN apk add libffi-dev openssl-dev cargo

RUN pip install --upgrade pip
RUN pip install gunicorn psycopg2 psycopg2-binary

COPY ./backend/requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000