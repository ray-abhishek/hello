FROM ubuntu:16.04

USER root

RUN apt-get update && apt-get install -y build-essential python-dev python-pip libgeos-dev python-dev swig libssl-dev libffi-dev libncurses5-dev \
                                         libjpeg-dev libfreetype6-dev zlib1g-dev libpq-dev libmysqlclient-dev inotify-tools tzdata wget libbz2-dev \
                                         libsqlite3-dev locales


RUN curl -sSL https://get.docker.com/ | sh
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

RUN wget -qO- https://deb.nodesource.com/setup_10.x | bash -
RUN apt update
RUN apt install -y nodejs
RUN npm install -g yarn
RUN yarn global add imagemin-cli@3.0.0 imagemin-mozjpeg@6.0.0 imagemin-pngquant@5.0.1

ADD docker-entrypoint.sh /usr/bin/docker-entrypoint
RUN chmod +x /usr/bin/docker-entrypoint
ENTRYPOINT ["docker-entrypoint"]

