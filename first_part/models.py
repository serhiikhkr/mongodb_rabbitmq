from mongoengine import Document
from mongoengine.fields import StringField, ReferenceField, ListField


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(required=True)
    born_location = StringField(required=True)
    description = StringField(required=True)

    # meta = {'db_alias': 'authors_and_quotes'}


class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author)
    quote = StringField(required=True)

    # meta = {'db_alias': 'authors_and_quotes'}

