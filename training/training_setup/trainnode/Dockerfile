#  @Author: Webster Bei Yijie, Joey Junyu Liang
#  @Date: 5/8/2020, 3:18:14 PM
#  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


FROM websterbei/pytorch-base:v1

ADD ./training_setup/trainnode/run.sh /run.sh
ADD ./training_src /training

RUN chmod a+x /run.sh

CMD ["/run.sh"]