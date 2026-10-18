"""Flask app factory."""
from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from .routes import notes_bp
    app.register_blueprint(notes_bp)

    with app.app_context():
        db.create_all()

    return app
