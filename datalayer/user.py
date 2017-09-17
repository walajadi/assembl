
from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField, EmailField,\
    URLField

connect('assembl')


class User(Document):
    username = StringField(unique=True)
    email = EmailField(unique=True)
    password = StringField()  # add encryption.
    created = DateTimeField()
    verified = BooleanField()
    avatar = URLField()
