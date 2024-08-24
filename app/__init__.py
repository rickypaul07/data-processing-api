from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = './uploads/'

    with app.app_context():
        # Import routes so they are registered with the app
        from . import routes
        return app
