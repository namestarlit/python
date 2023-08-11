from flask import render_template, url_for
from flask import flash, redirect

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

    index_page = render_template('index.html', title='Home',
                                 user=user, posts=posts)
    return index_page


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Defines login route."""
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'
              .format(form.username.data, form.remember_me.data)
              )
        return redirect(url_for('index'))
    login_page = render_template('login.html', title='Sign In', form=form)
    return login_page
