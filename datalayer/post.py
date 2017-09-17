
from mongoengine import connect, Document, ListField, StringField, BooleanField, DateTimeField, IntField
from datetime import datetime

connect('assembl')


class Post(Document):

    title = StringField()
    is_top = BooleanField()
    name = StringField()
    topics = ListField(StringField())
    created = DateTimeField(default=datetime.now())
    author = StringField()  # user_id
    content = StringField()
    likes = IntField()
    ideas = ListField(StringField())
    parent = StringField()  # post_id as str, empty if is_top

    def add_idea(self, idea):
        """
        Add idea to post.
        :param idea:
        :return:
        """
        self.ideas.append(str(idea.id))
        self.save()
