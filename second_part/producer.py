import pika
from faker import Faker
from mongoengine import connect
from models import Contact

fake = Faker()

connect(host="mongodb+srv://helloworld:goitserhii@serhii.n5tsqhh.mongodb.net/?retryWrites=true&w=majority", ssl=True)

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

for _ in range(10):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        sent=False
    )
    contact.save()

    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=str(contact.id))

connection.close()
