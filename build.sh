cd wordcount
javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-3.3.4.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar -d classes/ src/*.java
jar -cvf wordcount.jar classes
hadoop fs -rm -f -r /hbase/output/
hadoop jar wordcount.jar com.lisong.hadoop.WordCount /hbase/input /hbase/output