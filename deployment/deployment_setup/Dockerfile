#  @Author: Webster Bei Yijie, Joey Junyu Liang
#  @Date: 5/8/2020, 3:15:43 PM
#  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


FROM websterbei/pytorch-base:v1

RUN /miniconda/bin/conda install flask

ADD ./deployment_src /deployment

ADD ./deployment_setup/run.sh /run.sh
RUN chmod a+x /run.sh

EXPOSE 5000

ENTRYPOINT ["/run.sh"]