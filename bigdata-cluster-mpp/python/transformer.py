#!/usr/bin/python3                                                                                                      
import os                                                                                                                        
from pyspark import SparkContext                                                                                        
from pyspark.sql import SparkSession                                                                                    
from pyspark.streaming import StreamingContext                                                                          
from pyspark.streaming.kafka import KafkaUtils          
from utils import preprocess

import nltk
import pickle
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /spark/jar/spark-streaming-kafka-0-8-assembly_2.11-2.4.8.jar pyspark-shell'

def handle_rdd(rdd):                                                                                                    
    if not rdd.isEmpty():                                                                                               
        global ss                                                                                                       
        df = ss.createDataFrame(rdd, schema=['text', 'words', 'length', 'sentiment'])                                                
        df.show()                                                                                                       
        df.write.saveAsTable(name='default.tweets', format='hive', mode='append')                                       
print('transformer called...')                                                                                                                        
sc = SparkContext(appName="Something")                                                                                     
ssc = StreamingContext(sc, 5)                                                                                           
                                                                                                                        
ss = SparkSession.builder.appName("Something").config("spark.sql.warehouse.dir", "/user/hive/warehouse").config("hive.metastore.uris", "thrift://bigdata-cluster-hadoop:9083").enableHiveSupport().getOrCreate()                                                                                                  
                                                                                                                        
ss.sparkContext.setLogLevel('WARN')     

print('connecting to kafka')                                                                                
                                                                                                                        
ks = KafkaUtils.createDirectStream(ssc, ['tweets'], {'metadata.broker.list': 'kafka:9092'})                       

#sid = SentimentIntensityAnalyzer()
model = pickle.load(open("models/sentiment.pkl", "rb"))
                                                                                                                 
lines = ks.map(lambda x: x[1])                                                                                          
print('analysing the tweets')        

transform = lines.map(lambda tweet: (tweet, int(len(tweet.split())), int(len(tweet)), model.predict(preprocess(tweet))))                                  

transform.foreachRDD(handle_rdd)                                                                                        
                                                                                                                        
ssc.start()                                                                                                             
ssc.awaitTermination()

# CREATE TABLE tweets (text STRING, words INT, length INT, text STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\\|' STORED AS TEXTFILE;

print('done')