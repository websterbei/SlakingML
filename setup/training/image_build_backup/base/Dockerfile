FROM debian:9

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      python3 \
      python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN ln $(which pip3) /usr/bin/pip
RUN ln $(which python3) /usr/bin/python

RUN pip install torch

