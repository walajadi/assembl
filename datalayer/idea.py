
from datetime import datetime
from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField, DictField


connect('assembl')


class Idea(Document):

    title = StringField(required=True)
    description = StringField(required=True)
    created = DateTimeField(default=datetime.now())
    updated = DateTimeField()
    deleted = DateTimeField()
    posts = ListField(StringField())  # post id associated to this idea
    creator = StringField()  # user_id as str
    children_ideas = ListField(StringField())  # idea_ids list
    authorized_users = DictField()
