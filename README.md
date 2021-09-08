# Steps to run

## Terminal-1

docker exec -it bigdata-cluster-mpp bash

cd python

python3 model_generator.py

python3 house_producer.py

## Terminal-2

docker exec -it bigdata-cluster-mpp bash

cd python

python3 spark_consumer.py



# Kafka commands:

nohup bin/zookeeper-server-start.sh config/zookeeper.properties &

nohup bin/kafka-server-start.sh config/server.properties &

kafka-topics.sh --create --topic house --bootstrap-server 127.0.0.1:9092 --partitions 1 --replication-factor 1

topic content:
kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic house --from-beginning

