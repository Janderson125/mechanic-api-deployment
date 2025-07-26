# flask_app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import ProductionConfig
from routes.mechanic_routes import mechanic_bp
import os

app = Flask(__name__)
app.config.from_object(ProductionConfig)

db = SQLAlchemy(app)

app.register_blueprint(mechanic_bp, url_prefix="/mechanics")