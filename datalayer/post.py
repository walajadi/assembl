

from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField

connect('assembl')


class Post(Document):

    title = StringField()
    description = StringField()
    is_top = BooleanField()
    name = StringField()
    topics = ListField(StringField)
    created = DateTimeField()
    author = StringField()  # user_id
    content = StringField()
    likes = IntField()
    ideas = ListField(StringField)

    meta = {
        'db_alias': 'assembl'
    }

