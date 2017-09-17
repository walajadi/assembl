
from datalayer.user import User
from datalayer.discussion import Discussion
from datalayer.post import Post
from datalayer.idea import Idea


def set_global_permissions(user, permission):
    """
    give a global permission set to a user across all discussions.
    :param user:
    :param permission
    :return:
    """
    discussions = Discussion.objects()
    for discussion in discussions:
        discussion.autorize_user(str(user.id), permission)


def set_local_permission(discussion, user, permission):
    """
     given a discussion, set a local permission to a user for that discussion.
    :param discussion:
    :param user:
    :param permission:
    :return:
    """
    discussion.autorize_user(str(user.id), permission)


def all_posts_not_associated_to_idea(idea):
    """
    returns the set of all posts that are not associated to an Idea
    :param idea:
    :return:
    """
    posts = Post.objects(ideas__ne=str(idea.id))  # not equal to the input idea id
    return posts


def all_posts_associated_to_idea(idea):
    """
    returns a set of all posts associated to an idea
    :param idea:
    :return:
    """
    posts = Post.objects(ideas=str(idea.id))
    return posts

# FIXME : from my understanding, number_of_messages and all_posts_associated_to_idea are the same.


def number_of_messages(idea):
    """
    given an idea, return the number of unique messages on that idea
    :param idea:
    :return:
    """
    posts = Post.objects(ideas=str(idea.id))
    return posts


def number_of_participants(discussion):
    """
    given a discussion, return the number of participants who have contributed to the discussion
    :param idea:
    :return:
    """
    return discussion.number_of_participants()


def number_of_participants_on_idea(idea):
    """
    given an idea, return all participants have have contributed to it (posted in idea), and all sub ideas (inclusive)
    :param idea:
    :return:
    """
    sub_ideas = Idea.objects(ancestor=str(idea.id))
    all_posts_ids = []
    for sub_idea in sub_ideas:
        all_posts_ids.extend(sub_idea.post)

    all_users_ids = set([Post.objects.get(id=post_id).author for post_id in all_posts_ids if post_id])
    return len(all_users_ids)


def get_all_children_posts(parent_post):
    """
    return a list of all posts that are replies to the parent post, including their children
    :param parent_post
    :return:
    """
    return Post.objects(parent=str(parent_post.id))


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

    reply_to_post_1 = Post(**{'title': 'neh', 'content': 'o matter where you go Armand. the world isn\'t big enough to \
    hide from me.', 'author': str(user_2.id), 'is_top': False, 'parent': str(post_by_user_1.id)})

    reply_to_post_1.save()

    post_by_user_2 = Post(
        **{'title': 'lolita message', 'content': 'Your swordsmanship? Where did you learn the blade? ', \
           'author': str(user_2.id), 'is_top': True, 'likes': 50})
    post_by_user_2.save()

    reply_to_post_2 = Post(**{'title': 'lolita message', 'content': 'You\'re one blind Mexican. You don\'t know what you\'r\
    e getting yourself into.', 'author': str(user_1.id), 'is_top': False, 'parent': str(post_by_user_2.id)})

    reply_to_post_2.save()

    # create discussion
    discussion_1 = Discussion(
        **{'name': 'Justice', 'title': 'Mexican California is not fair', 'creator': str(user_1.id), \
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

    # sub_ideas.
    sub_idea_1 = Idea(
        **{'title': 'Save justice 2', 'description': 'philosophical theory by which fairness is administered.',
           'posts': [str(post_by_user_1.id)], 'creator': str(user_1.id), 'ancestor': str(idea_1.id)})
    sub_idea_1.save()

    sub_idea_2 = Idea(
        **{'title': 'Respect justice 2', 'description': 'it can only exist within the coordinates of equality.',
           'posts': [str(post_by_user_2.id)], 'creator': str(user_2.id), 'ancestor': str(idea_2.id)})
    sub_idea_2.save()

    # add ideas to discussion and posts
    discussion_1.add_idea(str(idea_1.id))
    discussion_1.add_idea(str(idea_2.id))
    post_by_user_1.add_idea(idea_1)
    post_by_user_1.add_idea(sub_idea_1)
    post_by_user_2.add_idea(idea_2)
    post_by_user_2.add_idea(sub_idea_2)
