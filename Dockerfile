# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/engine/reference/builder/

ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /home/src
RUN apt-get -y update
# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt 
    
RUN python -m pip install pytest-xvfb
RUN apt-get install tk -y
RUN apt-get install -y x11-apps
RUN apt-get update && apt-get install -y python3-opencv
RUN pip install opencv-python

# Copy the source code into the container.
COPY . .

CMD python3 View.py

