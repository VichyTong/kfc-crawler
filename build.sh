cd wordcount
javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-3.3.4.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar -d classes/ src/*.java
jar -cvf wordcount.jar classes
