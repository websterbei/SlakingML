FROM websterbei/pytorch-base:v1

RUN /miniconda/bin/conda install flask

ADD ./deployment_src /deployment

ADD ./deployment_setup/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 5000

ENTRYPOINT ["/run.sh"]