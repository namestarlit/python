from datetime import datetime

from microblog import db


class User(db.Model):
    """Defines a class User."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True,
                         nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        """String representantion of User class."""
        return ("<{}: (id={}, username='{}', email='{}')>"
                .format(self.__class__.__name__,
                        self.id, self.username,
                        self.email)
                )


class Post(db.Model):
    """Defines a class Post."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """String representantion of Post class."""
        return ("<{}: (id={}, timestamp='{}', user_id={})>"
                .format(self.__class__.__name__,
                        self.id,
                        self.timestamp,
                        self.user_id)
                )
