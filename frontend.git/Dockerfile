FROM python:3-alpine

MAINTAINER Peter Fisher

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  && pip install --upgrade pip  \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app /app

ENV PRODUCT_SERVICE 'http://192.168.43.61:30002'
ENV ORDER_SERVICE 'http://192.168.43.61:30003'
ENV USER_SERVICE 'http://192.168.43.61:30004'

CMD python app.py run -h 0.0.0.0

