from kafka import KafkaConsumer
import json
import time


#~~~ Configuration matches that of producer

consumer = KafkaConsumer(
    'stock_analysis',
    bootstrap_servers = ['localhost:9094'],
    auto_offset_reset = 'earliest',
    enable_auto_commit = True,
    group_id = 'my_consumer_group', # define a consumer group
    value_deserializer = lambda x: json.loads(x.decode('utf-8'))
)

print("Starting Kafka consumer. waiting for message on topic 'stock_analysis...")

for message in consumer:
    data = message.value

    # print the recieved value

    print(f" Value (Deserializer): {data}")

    consumer.close()

    print("Kafka consumer closed.")