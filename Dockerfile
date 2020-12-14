FROM centos/python-36-centos7

LABEL maintainer='john.adrift@gmail.com'

COPY . ./

CMD [ "python", "./rafi_adventure/" ]