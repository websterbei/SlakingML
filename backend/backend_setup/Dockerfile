#  @Author: Webster Bei Yijie, Joey Junyu Liang
#  @Date: 5/8/2020, 3:14:52 PM
#  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


FROM node

RUN mkdir /slaking-backend

RUN echo $(which node)

ADD ./slaking-backend/ /slaking-backend

EXPOSE 3000

RUN chmod a+x /slaking-backend/bin/www

WORKDIR /slaking-backend

CMD ["./bin/www"]

