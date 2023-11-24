import os
import sys

import pika
from mongoengine import connect
from models import Contact

connect(host="mongodb+srv://helloworld:goitserhii@serhii.n5tsqhh.mongodb.net/?retryWrites=true&w=majority", ssl=True)


def main():
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        send_email_stub(body.decode())

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


def send_email_stub(contact_id):
    contact = Contact.objects(id=contact_id).first()
    if contact:
        print(f"Sending email to {contact.email}")
        contact.sent = True
        contact.save()
    else:
        print(f"Contact with ID {contact_id} not found")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)