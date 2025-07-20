from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    # Import and register Blueprints
    from app.routes.mechanics import mechanics_bp
    from app.routes.tickets import tickets_bp
    from app.swagger.swagger_config import swaggerui_blueprint

    app.register_blueprint(mechanics_bp, url_prefix='/mechanics')
    app.register_blueprint(tickets_bp, url_prefix='/tickets')
    app.register_blueprint(swaggerui_blueprint, url_prefix='/docs')

    return app
