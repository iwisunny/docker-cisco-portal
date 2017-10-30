FROM centos:7.2.1511

MAINTAINER Mark Duan <markduan@yunify.com>

# Install dependencies
RUN yum -y install yum-plugin-ovl
RUN yum -y install yum-utils
RUN yum -y install epel-release
RUN yum -y install gcc
RUN yum -y install make
RUN yum -y install git
RUN yum -y install vim
RUN yum -y install zsh ntp
RUN yum -y install net-tools nc swig-doc.noarch
RUN yum -y install openssl-devel
RUN yum -y install python-devel python-pip

# Install dependencies for Python
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

ARG project_settings
ARG gunicorn_conf
ARG project_name

# Setup directories
# global memcached config
ADD ./pitrix/conf/global /pitrix/conf/global
# project settings
ADD ./pitrix/conf/$project_settings /pitrix/conf/
# gunicorn config
ADD ./gunicorn/$gunicorn_conf /etc/gunicorn/conf.py

COPY ./requirements.txt /pitrix/conf/global
RUN pip install -r /pitrix/conf/global/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

VOLUME "/pitrix/log"
VOLUME "/var/log/gunicorn"
VOLUME "/pitrix/lib/$project_name"

CMD gunicorn -c /etc/gunicorn/conf.py mysite.wsgi
