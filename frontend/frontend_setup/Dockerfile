FROM node

RUN npm install -g http-server

RUN mkdir /slaking-frontend

ADD ./slaking-frontend/dist /slaking-frontend

WORKDIR /slaking-frontend

EXPOSE 8080

CMD ["http-server", "./"]
