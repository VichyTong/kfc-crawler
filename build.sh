cd woordcount
javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-2.6.0.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.6.0.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar -d classes/ src/*.java
jar -cvf wordcount.jar classes
