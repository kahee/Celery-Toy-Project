FROM            python:3.6.4-slim

RUN             apt-get -y update
RUN             apt-get -y dist-upgrade
RUN             mkdir /code
COPY            requirements.text /code/requirements.txt
RUN             pip install --upgrade pip
RUN             pip install -r /code/requirements.txt


