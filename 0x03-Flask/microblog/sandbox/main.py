#!/usr/bin/env python3
"""Playing around with the database."""

from microblog import app, db
from microblog.models import User, Post


# Create an application context.
with app.app_context():
    user_1 = User(username='starlit', email='starlit@email.com')
    user_2 = User(username='rego', email='rego@email.com')
    user_3 = User(username='ed', email='ed@email.com')
    user_4 = User(username='susan', email='susan@email.com')

    #post_1 = Post(body="I love this blog", user_id=user_1)
    #post_2 = Post(body="I am the man", user_id=user_3)

    db.session.add(user_1)
    db.session.add(user_2)
    db.session.add(user_3)
    db.session.add(user_4)
    #db.session.add(post_1)
    #db.session.add(post_2)

    db.session.commit()

    users = db.session.execute(db.select(User).order_by(User.id))
    #posts = db.session.execute(db.select(Post).order_by(Post.user_id))

    users_list = users.scalars().all()
    #posts_list = posts.scalars().all()

    print(users_list)
    print()
    #print(posts_list)
