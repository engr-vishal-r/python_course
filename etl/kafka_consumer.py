from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': '172.17.22.218:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['kafka_topic_vb'])

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error:", msg.error())
        continue

    print(f"Received message: {msg.value().decode('utf-8')}")

c.close()