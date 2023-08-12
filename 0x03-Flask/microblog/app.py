#!/usr/bin/env python3
"""Main application module."""

from microblog import app, db
from microblog.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """Pre-imports the application instances."""
    instances = {
            'db': db,
            'User': User,
            'Post': Post
            }

    return instances


if __name__ == '__main__':
    app.run(debug=True)
