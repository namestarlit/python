from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes here to avoid circular imports.
from microblog import routes, models

# Create tables within an application context
#with app.app_context():
#    db.create_all()
