#!/usr/bin/python3
from kafka import KafkaProducer
import sys
import re
import pandas as pd
import json
import time
import random

KAFKA_BROKER = 'kafka:9092'
KAFKA_TOPIC = 'house'

try:
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
except Exception as e:
    print(f'Error Connecting to Kafka --> {e}')

df = pd.read_csv('data/test.csv')

print(df.head(2))

import json
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

for i in range(df.shape[0]):
    record_dict = df.iloc[i].to_dict()
    print("sending...", str(record_dict))
    producer.send(KAFKA_TOPIC, json.dumps(record_dict,cls=NpEncoder).encode("utf-8"))
    print('message sent to topic')
    time.sleep(random.randint(3,5))