FROM openjdk:8-jdk-alpine

MAINTAINER Buddha Jyothiprasad

#RUN apt-get update

#Install all the basic linux tools
RUN apk add --update bash vim bash-completion curl sudo bc

#Install all the languages/compilers we are supporting
RUN apk add --update gcc g++ python python3 py-pip mono ruby npm nodejs golang-go scala

RUN npm install -g underscore request express jade shelljs passport http sys jquery lodash async mocha moment connect validator restify ejs ws co when helmet wrench brain mustache should backbone forever  debug && export NODE_PATH=/usr/local/lib/node_modules/



