FROM ubuntu:16.10

RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install wget curl aptitude build-essential python3-dev
RUN apt-get -y install git

ADD run.sh /tmp/
CMD ["/bin/bash", "-c", "/tmp/run.sh"]
