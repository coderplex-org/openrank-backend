FROM debian:stretch-slim

MAINTAINER Buddha Jyothiprasad

RUN apt-get update

#Install all the basic linux tools
#RUN apt-get install -y --allow-unauthenticated vim
RUN apt-get install -y --allow-unauthenticated sudo
RUN apt-get install -y --allow-unauthenticated curl

#RUN apt-get install -y --allow-unauthenticated python3

#Install nodejs and some mostly used npm packages
RUN apt-get install -y --allow-unauthenticated gnupg2
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
RUN apt-get update
RUN apt-get install -y --allow-unauthenticated nodejs
RUN npm install -g underscore request express pug shelljs passport http sys jquery lodash async mocha moment connect validator restify ejs ws co when helmet fs-extra brain mustache should backbone forever debug && export NODE_PATH=/usr/local/lib/node_modules/

