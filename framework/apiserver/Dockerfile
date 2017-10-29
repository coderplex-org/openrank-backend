FROM docker:17.10-rc

MAINTAINER Buddha Jyothiprasad

RUN apt-get update

#Install all the basic linux tools
RUN apt-get install -y --allow-unauthenticated vim
RUN apt-get install -y --allow-unauthenticated sudo
RUN apt-get install -y --allow-unauthenticated curl

#Install all the basic linux tools
RUN apt-get install -y --allow-unauthenticated python3
RUN apt-get install -y --allow-unauthenticated python
RUN apt-get install -y --allow-unauthenticated python-pip
RUN apt-get install -y --allow-unauthenticated python3-pip
RUN pip install --upgrade pip
RUN pip install docker
RUN pip install django
RUN pip install djangorestframework


