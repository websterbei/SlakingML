FROM node

RUN mkdir /slaking-backend

RUN echo $(which node)

ADD ./slaking-backend/ /slaking-backend

EXPOSE 3000

RUN chmod a+x /slaking-backend/bin/www

CMD ["/slaking-backend/bin/www"]
