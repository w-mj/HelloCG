FROM python:3.7
MAINTAINER WMJ "wmj@alphamj.cn"
COPY kernel/ /
CMD bash test.sh
