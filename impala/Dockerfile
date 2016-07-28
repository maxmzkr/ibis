from ubuntu:14.04

RUN apt-get update -y && apt-get install wget -y

RUN wget 'https://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/cloudera.list' -O /etc/apt/sources.list.d/cloudera.list

RUN wget https://archive.cloudera.com/cdh5/ubuntu/trusty/amd64/cdh/archive.key -O archive.key && apt-key add archive.key

RUN apt-get update -y && apt-get install -y \
  bc \
  hadoop-hdfs-datanode \
  hadoop-hdfs-namenode \
  hive \
  hive-hbase \
  hive-metastore \
  hive-server2 \
  impala \
  impala-catalog \
  impala-server \
  impala-shell \
  impala-state-store \
  libpostgresql-jdbc-java \
  postgresql-client \
  wget


RUN mkdir -p /var/lib/hadoop-hdfs/cache/hdfs/dfs/name
RUN /usr/bin/hadoop namenode -format
RUN chown -R hdfs:hdfs /var/lib/hadoop-hdfs/cache/hdfs
RUN mkdir -p /var/run/hdfs-sockets
RUN chown -R hdfs:hdfs /var/run/hdfs-sockets

RUN ln -s /usr/share/java/postgresql-jdbc4.jar /usr/lib/hive/lib/postgresql-jdbc4.jar

COPY core-site.xml /etc/hadoop/conf/core-site.xml
COPY hdfs-site.xml /etc/hadoop/conf/hdfs-site.xml
COPY core-site.xml /etc/impala/conf/core-site.xml
COPY hdfs-site.xml /etc/impala/conf/hdfs-site.xml
COPY hive-site.xml /usr/lib/hive/conf/hive-site.xml
COPY hive-site.xml /etc/impala/conf/hive-site.xml

COPY init /init

CMD /init
