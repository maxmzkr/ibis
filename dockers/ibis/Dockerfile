FROM ubuntu:14.04

RUN apt-get update -y && apt-get install -y \
  wget

RUN wget -O - http://apt.llvm.org/llvm-snapshot.gpg.key|sudo apt-key add -

COPY llvm.list /etc/apt/sources.list.d/llvm.list

RUN apt-get update -y && apt-get install -y \
  clang-3.8 \
  cmake \
  postgresql-server-dev-9.3 \
  python-dev \
  python-pip

RUN ln -s /usr/bin/clang++-3.8 /usr/bin/clang++

ADD ./requirements.txt /requirements.txt

RUN pip install pip --upgrade
RUN pip install setuptools --upgrade

RUN pip install -r /requirements.txt

RUN pip install click

ENV PYTHONPATH=/ibis

CMD tail -f /dev/null
