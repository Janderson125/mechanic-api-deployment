from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_object=None):
    app = Flask(__name__)
    if config_object:
        app.config.from_object(config_object)

    db.init_app(app)

    # Use full package path starting from mechanic_api
    from mechanic_api.app.routes.mechanics import mechanics_bp
    from mechanic_api.app.routes.tickets import tickets_bp

    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
    app.register_blueprint(tickets_bp, url_prefix="/tickets")

    @app.route("/")
    def index():
        return "API is running"

    return app
