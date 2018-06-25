#redis 설치 부분 base로 이용하기
FROM            python:3.6.4-slim

RUN             apt-get -y update
RUN             apt-get -y dist-upgrade
RUN             mkdir /code
COPY            requirements.text /code/requirements.txt
RUN             pip install --upgrade pip
RUN             pip install -r /code/requirements.txt
COPY            . /code
RUN             apt-get update && apt-get install -y redis-server
EXPOSE          6379

WORKDIR         /code
