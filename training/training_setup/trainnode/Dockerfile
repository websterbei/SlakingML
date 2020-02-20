FROM websterbei/pytorch-base:v1

ADD ./training_setup/trainnode/run.sh /run.sh
ADD ./training_src /training

RUN chmod a+x /run.sh

CMD ["/run.sh"]