#!/usr/bin/env python
# encoding: utf-8

"""
consumer_rebalance_a.py a消费者
"""

import pickle
import uuid
import time
from kafka import KafkaConsumer
from kafka.structs import TopicPartition, OffsetAndMetadata
from kafka import ConsumerRebalanceListener

consumer = KafkaConsumer(
    bootstrap_servers=['127.0.0.1:9092'],
    group_id="test_group_1",
    client_id="{}".format(str(uuid.uuid4())),
    enable_auto_commit=False,
    key_deserializer=lambda k: pickle.loads(k),
    value_deserializer=lambda v: pickle.loads(v)
)

# 用来记录最新的偏移量信息.
consumer_offsets = {}


class MineConsumerRebalanceListener(ConsumerRebalanceListener):
    def on_partitions_revoked(self, revoked):
        """
        再均衡开始之前 下一轮poll之前触发
        :param revoked:
        :return:
        """
        print('再均衡开始之前被自动触发.')
        print(revoked, type(revoked))
        consumer.commit_async(offsets=consumer_offsets)

    def on_partitions_assigned(self, assigned):
        """
        再均衡完成之后  即将下一轮poll之前 触发
        :param assigned:
        :return:
        """
        print('在均衡完成之后自动触发.')
        print(assigned, type(assigned))


consumer.subscribe(topics=('zch',), listener=MineConsumerRebalanceListener())


def _on_send_response(*args, **kwargs):
    """
    提交偏移量涉及回调函数
    :param args:
    :param kwargs:
    :return:
    """
    if isinstance(args[1], Exception):
        print('偏移量提交异常. {}'.format(args[1]))
    else:
        print('偏移量提交成功')


try:
    start_time = time.time()
    while True:
        # 再均衡其实是在poll之前完成的
        consumer_records_dict = consumer.poll(timeout_ms=100)

        # 处理逻辑.
        for k, record_list in consumer_records_dict.items():
            for record in record_list:
                print("topic = {},partition = {},offset = {},key = {},value = {}".format(
                    record.topic, record.partition, record.offset, record.key, record.value)
                )

                consumer_offsets[
                    TopicPartition(record.topic, record.partition)
                ] = OffsetAndMetadata(
                    record.offset + 1, metadata='偏移量.'
                )

        try:
            consumer.commit_async(callback=_on_send_response)
            time.sleep(10)
        except Exception as e:
            print('commit failed', str(e))

except Exception as e:
    print(str(e))
finally:
    try:
        # 同步提交偏移量,在消费者异常退出的时候再次提交偏移量,确保偏移量的提交.
        consumer.commit()
        print("同步补救提交成功")
    except Exception as e:
        consumer.close()
