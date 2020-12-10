FROM ubuntu:16.04
RUN apt-get update && apt-get install -y build-essential python-dev python-pip libgeos-dev python-dev swig libssl-dev libffi-dev libncurses5-dev \
                                         libjpeg-dev libfreetype6-dev zlib1g-dev libpq-dev libmysqlclient-dev inotify-tools tzdata wget libbz2-dev \
                                         libsqlite3-dev locales


RUN cd /
RUN wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
RUN tar -xvf Python-2.7.12.tgz
WORKDIR Python-2.7.12

RUN ./configure --enable-ipv6
RUN make
RUN make install

RUN apt-get remove -y python-setuptools
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py

WORKDIR /server
RUN pip install Django==1.7 mysqlclient==1.4.6 pytest==4.6.11 pytest-cov==2.5.1 pytest-xdist==1.20.0
RUN ls