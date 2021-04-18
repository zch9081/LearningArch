#!/usr/bin/env python
# encoding: utf-8

from kafka import KafkaConsumer
from kafka.consumer.fetcher import ConsumerRecord

consumer = KafkaConsumer(
    bootstrap_servers=['127.0.0.1:9092'],
    group_id="simple_consumer",
    auto_offset_reset="earliest"
)

consumer.subscribe(topics=["zch", ])

for msg in consumer:
    assert isinstance(msg, ConsumerRecord)
    print(msg)
