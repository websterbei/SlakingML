FROM websterbei/pytorch-base:v1

ADD ./training_setup/trainnode/entrypoint.sh /entrypoint.sh
ADD ./training_src /training

RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]