import json
import kafka
import time

from kafka import KafkaProducer
from kafka import KafkaConsumer

KAFKA_TOPIC = "sytest-topic"

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers="kafka-local.kafkaplaypen.svc.cluster.local:9092"
)



#print("Topics are "+ topics)
while True:
    print (" entering in loop")
    for message in consumer:
        print("Sending notification")
        consumed_msg = json.loads(message.value.decode("utf-8"))
        print("message ois " + consumed_msg)