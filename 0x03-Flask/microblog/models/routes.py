from flask import render_template
from models import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Starlit'}
    page = render_template('index.html', user=user)
    return page
