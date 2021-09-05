import findspark
findspark.init()


import json
from pyspark import SparkContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext

sc = SparkContext(appName="HousePrice")                                                                                     
ssc = StreamingContext(sc, 60)   

TOPIC = 'house'
KAFKA_BROKERS = '127.0.0.1:9092'

print('creating stream...')

stream = KafkaUtils.createDirectStream(
                            ssc, 
                            [TOPIC], 
                            {"metadata.broker.list": KAFKA_BROKERS})

stream = stream.map(lambda x: json.loads(x[1]))
#stream = stream.map(lambda x: (x["_c0"], x["loan"]))

stream.pprint()

ssc.start()
ssc.awaitTermination()