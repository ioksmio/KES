# Address_Producer.py
from faker import Faker
from kafka import KafkaProducer
import json
from data import get_new_user
import time

fake = Faker()

def get_new_user():
    return {
        "name": fake.name(),
        "address": fake.address(),
        "year_of_birth": fake.year()
    }

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['W.X.Y.Z:9092'],
                         value_serializer=json_serializer)

if __name__ == "__main__":
    while 1 == 1:
        new_user = get_new_user()
        print(new_user)
        producer.send("new_user", new_user)
        time.sleep(2)