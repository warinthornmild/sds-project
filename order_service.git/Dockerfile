FROM python:3-alpine

MAINTAINER Peter Fisher

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  bash \
  curl \
  py-mysqldb \
  gcc \
  libc-dev \
  mariadb-dev \
  nodejs \
  npm \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app/package.json /app/package.json
RUN npm install

COPY ./app /app

ENV USER_SERVICE 'http://192.168.43.61:30004'

CMD ["python", "app.py"]

