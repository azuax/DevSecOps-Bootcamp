FROM python:3.9.7-slim

RUN apt-get update && apt-get -y upgrade

RUN useradd -r -s /bin/bash devsecops

ENV HOME /app
WORKDIR /app
ENV PATH="/app/.local/bin:${PATH}"

RUN chown -R devsecops:devsecops /app
USER devsecops

ENV FLASK_ENV=Production

ARG AWS_ACCESS_KEY_ID 
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_DEFAULT_REGION
ARG FLASK_SECRET_KEY

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION
ENV FLASK_SECRET_KEY $FLASK_SECRET_KEY

ADD ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r ./requirements.txt --user

COPY . /app
WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers=5"]