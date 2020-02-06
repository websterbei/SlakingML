FROM node

RUN mkdir /slaking-frontend

ADD ./slaking-frontend/ /slaking-frontend

RUN ls /slaking-frontend

EXPOSE 3000

RUN chmod a+x /slaking-frontend/www.sh

CMD ["/slaking-frontend/www.sh"]