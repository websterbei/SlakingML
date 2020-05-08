#  @Author: Webster Bei Yijie, Joey Junyu Liang
#  @Date: 5/8/2020, 3:15:59 PM
#  @Email: yijie.bei@duke.edu, junyu.liang@duke.edu


FROM node

RUN npm install -g http-server

RUN mkdir /slaking-frontend

ADD ./slaking-frontend/dist /slaking-frontend

WORKDIR /slaking-frontend

EXPOSE 8080

CMD ["http-server", "./"]
