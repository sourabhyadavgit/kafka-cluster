import json
import kafka
import time

from kafka import KafkaProducer
from kafka import KafkaConsumer

KAFKA_TOPIC = "sytest-topic"

producer = KafkaProducer(
#    ORDER_confirmed_TOPIC,
    bootstrap_servers="kafka-local.kafkaplaypen.svc.cluster.local:9092"
)
Prod_Limit = 2000
print("starting to produce now")
for i in range (1,Prod_Limit):
        data = {
            "order_id" : i,
            "user_id" : f"SY_{i}",
            "Test" : " Test message for test",
            "Test2" : " msg msg"
            }
        time.sleep(2)
        print(f"done sending{i}")
producer.send(
                KAFKA_TOPIC,
                json.dumps(data).encode("utf-8")
            )
producer.flush()
