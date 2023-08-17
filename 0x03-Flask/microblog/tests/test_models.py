import unittest
import os
from datetime import datetime, timedelta

from microblog import app, db
from microblog.models import User, Post


class UserModelCase(unittest.TestCase):
    """Testing User class."""
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
                'TEST_DATABASE_URL', 'sqlite://')

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_password_hashing(self):
        user = User(username='susan')
        user.set_password('cat')
        self.assertFalse(user.check_password('dog'))
        self.assertTrue(user.check_password('cat'))

    def test_avatar(self):
        user = User(username='john', email='john@email.com')
        self.assertEqual(
                user.avatar(128),
                ('https://www.gravatar.com/avatar/'
                 '41193cdbffbf06be0cdf231b28c54b18?d=identicon&s=128')
                )

    def test_follow(self):
        user_1 = User(username='john', email='john@email.com')
        user_2 = User(username='susan', email='susan@email.com')

        with app.app_context():
            db.session.add(user_1)
            db.session.add(user_2)
            db.session.commit()

            self.assertEqual(user_1.followed.all(), [])
            self.assertEqual(user_2.followers.all(), [])

            user_1.follow(user_2)
            db.session.commit()
            self.assertTrue(user_1.is_following(user_2))
            self.assertEqual(user_1.followed.count(), 1)
            self.assertEqual(user_1.followed.first().username, 'susan')
            self.assertEqual(user_2.followers.count(), 1)
            self.assertEqual(user_2.followers.first().username, 'john')

            user_1.unfollow(user_2)
            db.session.commit()
            self.assertFalse(user_1.is_following(user_2))
            self.assertEqual(user_1.followed.count(), 0)
            self.assertEqual(user_2.followers.count(), 0)

    def test_follow_posts(self):
        with app.app_context():
            # Create four users.
            u1 = User(username='john', email='john@email.com')
            u2 = User(username='susan', email='susan@email.com')
            u3 = User(username='mary', email='mary@email.com')
            u4 = User(username='david', email='david@email.com')

            db.session.add_all([u1, u2, u3, u4])
            db.session.commit()

            # Create four posts
            p1 = Post(body='Post from john', author=u1,
                      timestamp=datetime.now() + timedelta(seconds=1)
                      )
            p2 = Post(body='Post from susan', author=u2,
                      timestamp=datetime.now() + timedelta(seconds=4)
                      )
            p3 = Post(body='Post from mary', author=u3,
                      timestamp=datetime.now() + timedelta(seconds=3)
                      )
            p4 = Post(body='Post from david', author=u4,
                      timestamp=datetime.now() + timedelta(seconds=2)
                      )
            db.session.add_all([p1, p2, p3, p4])
            db.session.commit()

            # setup the followers
            u1.follow(u2)
            u1.follow(u4)
            u2.follow(u3)
            u3.follow(u4)
            db.session.commit()

            # check the followed posts for each user
            f1 = u1.followed_posts().all()
            f2 = u2.followed_posts().all()
            f3 = u3.followed_posts().all()
            f4 = u4.followed_posts().all()

            self.assertEqual(f1, [p1, p2, p4])
            self.assertEqual(f2, [p2, p3])
            self.assertEqual(f3, [p3, p4])
            self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)
