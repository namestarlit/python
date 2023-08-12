from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Import routes here to avoid circular imports.
from microblog import routes
