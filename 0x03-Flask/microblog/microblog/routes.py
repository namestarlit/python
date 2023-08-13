from flask import render_template, url_for
from flask import flash, redirect, request
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from werkzeug.urls import url_parse

from microblog import app, db
from microblog.forms import LoginForm, RegistrationForm
from microblog.models import User


@app.route('/')
@app.route('/index')
@login_required
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

    index_page = render_template('index.html', title='Home', posts=posts)
    return index_page


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Defines login route."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    login_page = render_template('login.html', title='Sign In', form=form)
    return login_page


@app.route('/logout')
def logout():
    """Defines the logout route."""
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Defines a register route."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data)
        user.set_password(form.password.data)

        # Add user to the database
        with app.app_context():
            db.session.add(user)
            db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    register_page = render_template('register.html', title='Register',
                                    form=form)
    return register_page


@app.route('/user/<username>')
@login_required
def user(username):
    """Defines user route."""
    user = User.query.filter_by(username=username).first_or_404()

    posts = [
            {'author': user, 'body': 'Test Post #1'},
            {'author': user, 'body': 'Test Post #2'}
            ]
    user_page = render_template('user.html', user=user, posts=posts)
    return user_page
