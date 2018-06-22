FROM            python:3.6.4-slim

RUN             apt-get -y update
RUN             apt-get -y dist-upgrade

COPY            requirements.text /code/requirements.txt

WORKDIR         /code
RUN             pip install --upgrade pip
RUN             pip install -r /code/requirements.txt


COPY            . /code/
WORKDIR         /code/app/