
from mongoengine import connect, Document, ListField, StringField, DateTimeField, DictField
from datetime import datetime

connect('assembl')


class Discussion(Document):

    ideas = ListField()
    posts = ListField()
    name = StringField(required=True)
    title = StringField(required=True)
    description = StringField(required=True)
    created = DateTimeField(default=datetime.now())
    topics = ListField(default=None)
    creator = StringField(required=True)  # user_id as str
    authorized_users = DictField(default={'read': [], 'post': []})

    def create_post(self, post):
        """
        Add a post to a discussion
        :param post:
        :return:
        """
        user_id = post.author
        if user_id in self.authorized_users['post']:
            self.posts.insert(0, str(post.id))
            self.save()
            return True
        return False

    def delete_post(self, post):
        """
        Delete a post in discussion.
        :param post:
        :return:
        """
        self.posts.remove(str(post.id))
        self.save()

    def add_idea(self, idea_id):
        """
        create an idea in a discussion, as a root idea or a subidea, if creator has permission
        :return:
        """
        self.ideas.append(idea_id)
        self.save()

    def autorize_user(self, user_id, permission):
        """
        Add user and authorization : read or post.
        :param user_id:
        :param permission:
        :return:
        """
        self.authorized_users[permission].append(user_id)
        self.save()

    def number_of_participants(self):
        """
        given a discussion, return the number of participants who have contributed to the discussion.
        :return:
        """
        return len(set([post.author for post in self.posts]))
