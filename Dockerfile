FROM ubuntu:17.10

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN apt-get install -y npm

ADD [ ".", "/var/www/_game_chats/" ]
WORKDIR /var/www/_game_chats/


RUN pip3 install -r requirements/base.txt
RUN pip3 install -r requirements/local.txt
RUN npm install

EXPOSE 8001