FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

COPY ./rafi_adventure .

ENTRYPOINT [ "python", "rafi_adventure/" ]