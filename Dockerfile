FROM jupyter/base-notebook
MAINTAINER WMJ "wmj@alphamj.cn"
COPY kernel/ /
CMD python /test.py
