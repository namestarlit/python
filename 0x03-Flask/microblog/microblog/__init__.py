import logging
from logging.handlers import SMTPHandler

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

# Log errors by email.
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None

        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'],
                    app.congig['MAIL_PASSWORD']
                    )
            secure = None

            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                    mailhost=(
                        app.config['MAIL_SERVER'],
                        app.config['MAIL_PORT']),
                    fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                    toaddrs=app.config['ADMINS'], subject='Microblog Failure',
                    credentials=auth, secure=secure
                    )
            mail_handler.setLevel(loggin.ERROR)
            app.logger.addHandler(mail_handler)
