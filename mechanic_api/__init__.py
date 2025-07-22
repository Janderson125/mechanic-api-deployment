from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object=None):
    app = Flask(__name__)
    if config_object:
        app.config.from_object(config_object)

    db.init_app(app)

    from app.routes.mechanics import mechanics_bp
    from app.routes.tickets import tickets_bp

    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
    app.register_blueprint(tickets_bp, url_prefix="/tickets")

    return app
