<<<<<<< HEAD
# config.py
import os

class ProductionConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# models.py
from flask_app import db

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
=======
import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-should-set-a-secret-key')  # fallback for local dev

class DevelopmentConfig(Config):
    # Use your local MySQL credentials here for development
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Austin78702!@localhost/ecommerce_api'
    DEBUG = True

class ProductionConfig(Config):
    # For production, get DB URL and SECRET_KEY from environment variables (like Render)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = False
>>>>>>> 17b5f132d4177f1e7880cc3fdf6ba5a8bef6abcc
