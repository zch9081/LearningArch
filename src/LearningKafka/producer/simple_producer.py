#!/usr/bin/env python
# encoding: utf-8

from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['127.0.0.1:9092']
)

for i in range(10):
    value = bytes('topic_zch_' + str(i), encoding='utf-8')
    future = producer.send("zch", value)
    result = future.get(timeout=10)
    print(result)
