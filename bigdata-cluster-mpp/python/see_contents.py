from os.path import abspath
from pyspark.sql import SparkSession
from pyspark.sql import Row

if __name__ == "__main__":
    warehouse_location = "/user/hive/warehouse"

    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL Hive integration example") \
        .config("spark.sql.warehouse.dir", warehouse_location) \
        .enableHiveSupport() \
        .getOrCreate()

    ss = SparkSession.builder.appName("Reading").config("spark.sql.warehouse.dir", "/user/hive/warehouse").config("hive.metastore.uris", "thrift://bigdata-cluster-hadoop:9083").enableHiveSupport().getOrCreate()

    # Queries are expressed in HiveQL
    sql_output = spark.sql("SELECT * FROM default.tweets")
    print(sql_output)
    for record in sql_output.collect():
        print(record)
    spark.stop()

