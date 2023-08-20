#!/usr/bin/env python3
"""connecting to MySQL DBMS using Flask-SQLAlchemy."""
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL',
        'mysql+mysqldb://app_test:App_test_v0.1@localhost/app_test_db'
        )
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port='5000', debug=True)
