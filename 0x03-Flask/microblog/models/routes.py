from flask import render_template

from models import app
from models.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Starlit'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day on Portland!'
                },
            {
                'author': {'username': 'Susan'},
                'body': 'The Avengers movie was so cool!'
                }
            ]

    page = render_template('index.html', title='Home', user=user, posts=posts)
    return page


@app.route('/login')
def login():
    """Defines login route."""
    form = LoginForm()
    page = render_template('login.html', title='Sign In', form=form)
    return page
