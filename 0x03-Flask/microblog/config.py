import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """A Flask configuration class."""
    # Get secret key otherwise assign a default value.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')

    # SQLAlchemy configuration.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///'
                                             + os.path.join(basedir, 'app.db')
                                             )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
