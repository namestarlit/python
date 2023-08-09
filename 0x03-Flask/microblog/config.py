import os


class Config(object):
    """A Flask configuration class."""
    # Get secret key otherwise assign a default value.
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
