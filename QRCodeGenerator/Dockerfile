#
#  ArduTracker Server
#
#  Collector
#

FROM python:3.9-buster
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt

CMD tail -f /dev/null
