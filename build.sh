cd wordcount
javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-3.3.4.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.3.4.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar -d classes/ src/*.java
jar -cvf WordCount.jar classes
hadoop fs -rm -f /hbase/input/*
hadoop fs -rm -put input/jieba_result.txt /hbase/input/
hadoop fs -rm -f -r /hbase/output/
hadoop jar WordCount.jar com.lisong.hadoop.WordCount /hbase/input /hbase/output