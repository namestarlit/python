from app import create_app


# Create app instance
app = create_app()


@app.route('/')
@app.route('/index')
def index():
    return "Hello, Flask!"
