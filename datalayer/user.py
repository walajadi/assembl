
from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField, EmailField,\
    UrlField

connect('assembl')


class User(Document):

    username = StringField()
    email = EmailField()
    password = StringField()
    created = DateTimeField()
    verified = BooleanField()
    avatar = UrlField()

    meta = {
        'db_alias': 'assembl'
    }



