FROM            python:3.6.4-slim

RUN             apt-get -y update
RUN             apt-get -y dist-upgrade
RUN             apt-get -y install wget
RUN             wget http://download.redis.io/redis-stable.tar.gz && tar xvzf redis-stable.tar.gz
RUN             apt-get install -y make gcc tcl build-essential
RUN             mkdir /code
COPY            requirements.text /code/requirements.txt
RUN             pip install --upgrade pip
RUN             pip install -r /code/requirements.txt


