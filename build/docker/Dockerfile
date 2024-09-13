FROM ubuntu:jammy

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

ENV LANG en_US.UTF-8;
ENV LANGUAGE en_US:en;

FROM python:3.10.14-slim-bookworm

COPY requirements.txt /etc/
RUN pip3 install --no-cache-dir -r /etc/requirements.txt; \
    apt-get autoremove -y && \
    apt-get clean

