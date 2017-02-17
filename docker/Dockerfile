FROM ubuntu:16.10

RUN apt-get update
RUN apt-get -y install apt-utils
RUN apt-get -y install wget curl aptitude build-essential python3-dev

ADD run.sh /tmp/
CMD ["/tmp/run.sh"]
