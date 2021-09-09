# Steps to run

## Terminal-1 (Build and start container)

Step-1> docker-compose up

## Terminal-2 (Train model, Start Producer)

Step-2> docker exec -it bigdata-cluster-mpp bash

Step-3> cd python

Step-4> python3 model_generator.py

<img width="996" alt="model" src="https://user-images.githubusercontent.com/22998245/132731754-bb70bf35-068a-4781-a74a-1ffb8b422387.png">

Step-5> python3 house_producer.py

<img width="1680" alt="Producer" src="https://user-images.githubusercontent.com/22998245/132708630-e93807ab-9c53-4fc5-a68b-f4f2ae677698.png">


## Terminal-3 (Consumer with Predictor)

Step-6> docker exec -it bigdata-cluster-mpp bash

Step-7> cd python

Step-8> python3 spark_consumer.py

<img width="1574" alt="Consumer" src="https://user-images.githubusercontent.com/22998245/132708677-09840c58-b0b6-440c-95ea-bd70a711cfd1.png">

# Kafka commands:

- To start zookeeper service

  nohup bin/zookeeper-server-start.sh config/zookeeper.properties &

- To start kafka server

  nohup bin/kafka-server-start.sh config/server.properties &

- To create topic manually

  kafka-topics.sh --create --topic house --bootstrap-server 127.0.0.1:9092 --partitions 1 --replication-factor 1

- To list all topics

  kafka-topics.sh --list --bootstrap-server 127.0.0.1:9092

<img width="941" alt="Kafka Topic" src="https://user-images.githubusercontent.com/22998245/132708834-660955dd-806c-4a88-ad6f-cbf24d69145b.png">


- To view topic contents

  kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic house --from-beginning

<img width="1680" alt="Kafka Content" src="https://user-images.githubusercontent.com/22998245/132709061-a3d45a9a-8487-4ad3-834f-e5869e8eccb4.png">


## Model training - Notebook

Trained and compared three models Random forest Regression, XGboost Regression, Linear Regression

Notebook Name: DataAnalysisAndModelCreation.ipynb
 
