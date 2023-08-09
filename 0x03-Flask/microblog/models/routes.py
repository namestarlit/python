from flask import render_template

from models import app


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
