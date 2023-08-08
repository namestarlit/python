from flask import Flask


def create_app():
    """Creates an instance of app."""
    app = Flask(__name__)

    # Import routes here to avoid circular imports.
    from app import routes

    return app
