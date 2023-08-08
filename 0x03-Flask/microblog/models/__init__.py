from flask import Flask

app = Flask(__name__)

# Import routes here to avoid circular imports.
from models import routes
