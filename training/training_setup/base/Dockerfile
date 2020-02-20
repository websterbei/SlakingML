FROM websterbei/hadoop-base:v1

HEALTHCHECK CMD curl -f http://localhost:9864/ || exit 1
ENV HDFS_CONF_dfs_datanode_data_dir=file:///hadoop/dfs/data
RUN mkdir -p /hadoop/dfs/data

EXPOSE 9864

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      wget \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN /bin/bash ~/miniconda.sh -b -p /miniconda

RUN /miniconda/bin/conda install pymongo pytorch pyarrow hdfs3 libhdfs3 -c conda-forge

