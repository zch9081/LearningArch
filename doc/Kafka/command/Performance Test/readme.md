## kafka-producer-perf-test

```
usage: producer-performance [-h] --topic TOPIC --num-records NUM-RECORDS [--payload-delimiter PAYLOAD-DELIMITER] --throughput THROUGHPUT [--producer-props PROP-NAME=PROP-VALUE [PROP-NAME=PROP-VALUE ...]]
                            [--producer.config CONFIG-FILE] [--print-metrics] [--transactional-id TRANSACTIONAL-ID] [--transaction-duration-ms TRANSACTION-DURATION] (--record-size RECORD-SIZE |
                            --payload-file PAYLOAD-FILE)

This tool is used to verify the producer performance.

optional arguments:
  -h, --help             show this help message and exit
  --topic TOPIC          produce messages to this topic
  --num-records NUM-RECORDS
                         number of messages to produce
  --payload-delimiter PAYLOAD-DELIMITER
                         provides delimiter to be used when --payload-file is provided. Defaults to new line. Note that this parameter will be ignored if --payload-file is not provided. (default: \n)
  --throughput THROUGHPUT
                         throttle maximum message throughput to *approximately* THROUGHPUT messages/sec. Set this to -1 to disable throttling.
  --producer-props PROP-NAME=PROP-VALUE [PROP-NAME=PROP-VALUE ...]
                         kafka producer related configuration properties like bootstrap.servers,client.id etc. These configs take precedence over those passed via --producer.config.
  --producer.config CONFIG-FILE
                         producer config properties file.
  --print-metrics        print out metrics at the end of the test. (default: false)
  --transactional-id TRANSACTIONAL-ID
                         The transactionalId to use if transaction-duration-ms is > 0. Useful when testing the performance of concurrent transactions. (default: performance-producer-default-transactional-
                         id)
  --transaction-duration-ms TRANSACTION-DURATION
                         The max age of each transaction. The commitTransaction will be called after this time has elapsed. Transactions are only enabled if this value is positive. (default: 0)

  either --record-size or --payload-file must be specified but not both.

  --record-size RECORD-SIZE
                         message size in bytes. Note that you must provide exactly one of --record-size or --payload-file.
  --payload-file PAYLOAD-FILE
                         file to read the message payloads from. This works only for UTF-8 encoded text  files.  Payloads  will  be read from this file and a payload will be randomly selected when sending
                         messages. Note that you must provide exactly one of --record-size or --payload-file.
```

```shell
kafka-producer-perf-test --topic round_topic --num-records 1000 --producer.config producer.properties --print-metrics --throughput 100 --record-size 1024
```

### `--print-metrics` 参数

如果增加参数`--print-metrics`，会在脚本运行结束前打印出一些度量指标。

```shell
Metric Name                                                                           Value
app-info:commit-id:{client-id=producer-1}                                           : d19b95317d02f231
app-info:start-time-ms:{client-id=producer-1}                                       : 1615888857494
app-info:version:{client-id=producer-1}                                             : 6.1.0-ce
kafka-metrics-count:count:{client-id=producer-1}                                    : 106.000
producer-metrics:batch-size-avg:{client-id=producer-1}                              : 1143.809
producer-metrics:batch-size-max:{client-id=producer-1}                              : 15556.000
producer-metrics:batch-split-rate:{client-id=producer-1}                            : 0.000
producer-metrics:batch-split-total:{client-id=producer-1}                           : 0.000
producer-metrics:buffer-available-bytes:{client-id=producer-1}                      : 33554432.000
producer-metrics:buffer-exhausted-rate:{client-id=producer-1}                       : 0.000
producer-metrics:buffer-exhausted-total:{client-id=producer-1}                      : 0.000
producer-metrics:buffer-total-bytes:{client-id=producer-1}                          : 33554432.000
producer-metrics:bufferpool-wait-ratio:{client-id=producer-1}                       : 0.000
producer-metrics:bufferpool-wait-time-total:{client-id=producer-1}                  : 0.000
producer-metrics:compression-rate-avg:{client-id=producer-1}                        : 1.000
producer-metrics:connection-close-rate:{client-id=producer-1}                       : 0.000
producer-metrics:connection-close-total:{client-id=producer-1}                      : 0.000
producer-metrics:connection-count:{client-id=producer-1}                            : 2.000
producer-metrics:connection-creation-rate:{client-id=producer-1}                    : 0.050
producer-metrics:connection-creation-total:{client-id=producer-1}                   : 2.000
producer-metrics:failed-authentication-rate:{client-id=producer-1}                  : 0.000
producer-metrics:failed-authentication-total:{client-id=producer-1}                 : 0.000
producer-metrics:failed-handshake-rate:{client-id=producer-1}                       : 0.000
producer-metrics:failed-handshake-total:{client-id=producer-1}                      : 0.000
producer-metrics:failed-reauthentication-rate:{client-id=producer-1}                : 0.000
producer-metrics:failed-reauthentication-total:{client-id=producer-1}               : 0.000
producer-metrics:handshake-time-ns-avg:{client-id=producer-1}                       : NaN
producer-metrics:handshake-time-ns-max:{client-id=producer-1}                       : NaN
producer-metrics:incoming-byte-rate:{client-id=producer-1}                          : 1681.124
producer-metrics:incoming-byte-total:{client-id=producer-1}                         : 66902.000
producer-metrics:io-ratio:{client-id=producer-1}                                    : 0.003
producer-metrics:io-time-ns-avg:{client-id=producer-1}                              : 39710.853
producer-metrics:io-wait-ratio:{client-id=producer-1}                               : 0.235
producer-metrics:io-wait-time-ns-avg:{client-id=producer-1}                         : 3280686.193
producer-metrics:io-waittime-total:{client-id=producer-1}                           : 9409008001.000
producer-metrics:iotime-total:{client-id=producer-1}                                : 113890726.000
producer-metrics:metadata-age:{client-id=producer-1}                                : 9.758
producer-metrics:network-io-rate:{client-id=producer-1}                             : 48.093
producer-metrics:network-io-total:{client-id=producer-1}                            : 1914.000
producer-metrics:outgoing-byte-rate:{client-id=producer-1}                          : 28886.468
producer-metrics:outgoing-byte-total:{client-id=producer-1}                         : 1149537.000
producer-metrics:produce-throttle-time-avg:{client-id=producer-1}                   : 0.000
producer-metrics:produce-throttle-time-max:{client-id=producer-1}                   : 0.000
producer-metrics:reauthentication-latency-avg:{client-id=producer-1}                : NaN
producer-metrics:reauthentication-latency-max:{client-id=producer-1}                : NaN
producer-metrics:record-error-rate:{client-id=producer-1}                           : 0.000
producer-metrics:record-error-total:{client-id=producer-1}                          : 0.000
producer-metrics:record-queue-time-avg:{client-id=producer-1}                       : 0.106
producer-metrics:record-queue-time-max:{client-id=producer-1}                       : 10.000
producer-metrics:record-retry-rate:{client-id=producer-1}                           : 0.000
producer-metrics:record-retry-total:{client-id=producer-1}                          : 0.000
producer-metrics:record-send-rate:{client-id=producer-1}                            : 25.167
producer-metrics:record-send-total:{client-id=producer-1}                           : 1000.000
producer-metrics:record-size-avg:{client-id=producer-1}                             : 1110.000
producer-metrics:record-size-max:{client-id=producer-1}                             : 1110.000
producer-metrics:records-per-request-avg:{client-id=producer-1}                     : 1.048
producer-metrics:request-latency-avg:{client-id=producer-1}                         : 0.583
producer-metrics:request-latency-max:{client-id=producer-1}                         : 7.000
producer-metrics:request-rate:{client-id=producer-1}                                : 24.046
producer-metrics:request-size-avg:{client-id=producer-1}                            : 1201.188
producer-metrics:request-size-max:{client-id=producer-1}                            : 15617.000
producer-metrics:request-total:{client-id=producer-1}                               : 957.000
producer-metrics:requests-in-flight:{client-id=producer-1}                          : 0.000
producer-metrics:response-rate:{client-id=producer-1}                               : 24.048
producer-metrics:response-total:{client-id=producer-1}                              : 957.000
producer-metrics:select-rate:{client-id=producer-1}                                 : 71.714
producer-metrics:select-total:{client-id=producer-1}                                : 2868.000
producer-metrics:successful-authentication-no-reauth-total:{client-id=producer-1}   : 0.000
producer-metrics:successful-authentication-rate:{client-id=producer-1}              : 0.000
producer-metrics:successful-authentication-total:{client-id=producer-1}             : 0.000
producer-metrics:successful-reauthentication-rate:{client-id=producer-1}            : 0.000
producer-metrics:successful-reauthentication-total:{client-id=producer-1}           : 0.000
producer-metrics:waiting-threads:{client-id=producer-1}                             : 0.000
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node--1}    : 14.951
producer-node-metrics:incoming-byte-rate:{client-id=producer-1, node-id=node-1}     : 1668.604
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node--1}   : 595.000
producer-node-metrics:incoming-byte-total:{client-id=producer-1, node-id=node-1}    : 66307.000
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node--1}    : 2.412
producer-node-metrics:outgoing-byte-rate:{client-id=producer-1, node-id=node-1}     : 28926.215
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node--1}   : 96.000
producer-node-metrics:outgoing-byte-total:{client-id=producer-1, node-id=node-1}    : 1149441.000
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node--1}   : NaN
producer-node-metrics:request-latency-avg:{client-id=producer-1, node-id=node-1}    : 0.583
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node--1}   : NaN
producer-node-metrics:request-latency-max:{client-id=producer-1, node-id=node-1}    : 7.000
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node--1}          : 0.050
producer-node-metrics:request-rate:{client-id=producer-1, node-id=node-1}           : 24.032
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node--1}      : 48.000
producer-node-metrics:request-size-avg:{client-id=producer-1, node-id=node-1}       : 1203.603
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node--1}      : 53.000
producer-node-metrics:request-size-max:{client-id=producer-1, node-id=node-1}       : 15617.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node--1}         : 2.000
producer-node-metrics:request-total:{client-id=producer-1, node-id=node-1}          : 955.000
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node--1}         : 0.050
producer-node-metrics:response-rate:{client-id=producer-1, node-id=node-1}          : 24.032
producer-node-metrics:response-total:{client-id=producer-1, node-id=node--1}        : 2.000
producer-node-metrics:response-total:{client-id=producer-1, node-id=node-1}         : 955.000
producer-topic-metrics:byte-rate:{client-id=producer-1, topic=round_topic}          : 27463.167
producer-topic-metrics:byte-total:{client-id=producer-1, topic=round_topic}         : 1091194.000
producer-topic-metrics:compression-rate:{client-id=producer-1, topic=round_topic}   : 1.000
producer-topic-metrics:record-error-rate:{client-id=producer-1, topic=round_topic}  : 0.000
producer-topic-metrics:record-error-total:{client-id=producer-1, topic=round_topic} : 0.000
producer-topic-metrics:record-retry-rate:{client-id=producer-1, topic=round_topic}  : 0.000
producer-topic-metrics:record-retry-total:{client-id=producer-1, topic=round_topic} : 0.000
producer-topic-metrics:record-send-rate:{client-id=producer-1, topic=round_topic}   : 25.168
producer-topic-metrics:record-send-total:{client-id=producer-1, topic=round_topic}  : 1000.000
```
