# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /home/src
RUN apt-get -y update
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt 
    
RUN python -m pip install pytest-xvfb
RUN apt-get install tk -y
RUN apt-get install -y x11-apps
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

COPY . .

CMD python3 View.py

