FROM ubuntu

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh --no-check-certificate -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /miniconda

RUN /miniconda/bin/conda install pytorch flask pymongo

ADD ./deployment_src /deployment

ADD ./deployment_setup/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 5000

ENTRYPOINT ["/run.sh"]