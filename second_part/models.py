from mongoengine import Document, StringField, BooleanField


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    sent = BooleanField(default=False)

    meta = {'collection': 'contacts'}
