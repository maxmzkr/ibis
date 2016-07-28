FROM ubuntu:14.04

RUN apt-get update -y && apt-get install -y \
  wget

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -

COPY llvm.list /etc/apt/sources.list.d/llvm.list

RUN apt-get update -y && apt-get install -y \
  clang-3.8 \
  postgresql-server-dev-9.3 \
  python-dev \
  python-pip

ADD ../requirements.txt /requirements.txt

RUN pip install pip --upgrade
RUN pip install setuptools --upgrade

RUN pip install -r /requirements.txt

CMD /bin/bash
