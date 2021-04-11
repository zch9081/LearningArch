#!/usr/bin/env python
# encoding: utf-8

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092']
)

for i in range(10):
    value = 'topic_zch_' + str(i)
    future = producer.send("zch", value)
    result = future.get(timeout=10)
    print(result)
