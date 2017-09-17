
from datalayer.user import User
from datalayer.discussion import Discussion
from datalayer.post import Post
from datalayer.idea import Idea

def set_global_permissions(user):
    """
    give a global permission set to a user across all discussions.
    :param user:
    :return:
    """
    pass

def all_posts_not_associated_to_idea(idea):
    """
    returns the set of all posts that are not associated to an Idea
    :param idea:
    :return:
    """
    pass

def all_posts_associated_to_idea(idea):
    """
    returns a set of all posts associated to an idea
    :param idea:
    :return:
    """
    pass

if __name__ == '__main__':

    # create some users
    user_1 = User(**{'username': 'zorro', 'email': 'markof@zorro.com', 'password': 'asdf123', 'verified': True,
                   'avatar': 'https://en.wikipedia.org/wiki/Zorro#/media/File:Zorro_(Diego_de_la_Vega).jpg'})
    user_1.save()

    user_2 = User(**{'username': 'lolita', 'email': 'lolita@quintero.com', 'password': 'qwert123', 'verified': True,
                   'avatar': 'https://en.wikipedia.org/wiki/Zorro#/media/File:Zorro_(Diego_de_la_Vega).jpg'})
    user_2.save()

    # create some posts

    post_by_user_1 = Post(**{'title': 'zorro message', 'content': 'Justice for all! Punishment for the oppressors of the\
     helpless - from the governor down.', 'author': str(user_1.id), 'is_top': True, 'likes': 100})

    post_by_user_1.save()

    post_by_user_2 = Post(**{'title': 'lolita message', 'content': 'Your swordsmanship? Where did you learn the blade? ',\
                             'author': str(user_2.id), 'is_top': True, 'likes': 50})
    post_by_user_2.save()

    # create discussion
    discussion_1 = Discussion(**{'name': 'Justice', 'title': 'Mexican California is not fair', 'creator': str(user_1.id),\
                                  'topics': [], 'description': 'all matters linked to justice are discussed here.'})

    discussion_1.save()

    # handle authorization
    discussion_1.autorize_user(str(user_1.id), 'post')
    discussion_1.autorize_user(str(user_2.id), 'post')

    # add posts to discussion
    discussion_1.create_post(post_by_user_1)
    discussion_1.create_post(post_by_user_2)

    # create an idea from post
    idea_1 = Idea(**{'title': 'Save justice', 'description': 'philosophical theory by which fairness is administered.',
                     'posts': [str(post_by_user_1.id)], 'creator': str(user_1.id)})
    idea_1.save()

    idea_2 = Idea(**{'title': 'Respect justice', 'description': 'it can only exist within the coordinates of equality.',
                     'posts': [str(post_by_user_2.id)], 'creator': str(user_2.id)})
    idea_2.save()

    # add ideas to discussion
    discussion_1.add_idea(str(idea_1.id))
    discussion_1.add_idea(str(idea_2.id))
