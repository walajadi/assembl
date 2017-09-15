
from mongoengine import connect, Document, ListField, StringField

connect('assembl')


class Discussion(Document):

    ideas = ListField()
    posts = ListField()
    name = StringField()
    title = StringField()
    description = StringField()
    topics = ListField()

    meta = {
        'db_alias': 'assembl'
    }

