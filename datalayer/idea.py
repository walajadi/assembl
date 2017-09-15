
from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField

connect('assembl')


class Idea(Document):

    title = StringField()
    description = StringField()
    created = DateTimeField()
    updated = DateTimeField()
    deleted = DateTimeField()
    post = StringField()  # post id

    meta = {
        'db_alias': 'assembl'
    }
