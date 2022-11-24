FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/TestAuto
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/TestAuto
