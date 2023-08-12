from microblog import db


class User(db.Model):
    """Defines a class User."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """String representantion of User class."""
        return ("<{}: (id={}, username='{}', email='{}')>"
                .format(self.__class__.__name__,
                        self.id, self.username,
                        self.email)
                )
