"""
To start spark, run:
`aws emr create-cluster --name SparkCluster --ami-version 3.2.1 --instance-type m3.xlarge --instance-count 3 --ec2-attributes KeyName="Cornell Macbook" --applications Name=Hive --bootstrap-actions Path=s3://support.elasticmapreduce/spark/install-spark`

To login, run:
`aws emr ssh --cluster-id j-1B48P13XQ7QAB --key-pair-file ~/.ssh/CornellMacbook.pem`

To start spark, run
`MASTER=yarn-client /home/hadoop/spark/bin/spark-shell`

To start pyspark, run
`MASTER=yarn-client /home/hadoop/spark/bin/pyspark`

To shut down, run
`aws emr terminate-clusters --cluster-id j-367J67T8QGKAD`

For the short instructions, see:
- http://blogs.aws.amazon.com/bigdata/post/Tx15AY5C50K70RV/Installing-Apache-Spark-on-an-Amazon-EMR-Cluster

For more information, go see:
- https://aws.amazon.com/articles/4926593393724923
- http://docs.aws.amazon.com/ElasticMapReduce/latest/DeveloperGuide/emr-connect-master-node-ssh.html
- http://docs.aws.amazon.com/cli/latest/reference/emr/index.html
"""
