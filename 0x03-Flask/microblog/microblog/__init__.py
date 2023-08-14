from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from config import Config

app = Flask(__name__)
# Set strict_slashes to False globally
app.url_map.strict_slashes = False

# Set configuration from Configuration class.
app.config.from_object(Config)

# Login session instances.
login = LoginManager(app)
login.login_view = 'login'

# Database instances
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes here to avoid circular imports.
from microblog import routes, models, errors

# Create tables within an application context
#with app.app_context():
#    db.create_all()
