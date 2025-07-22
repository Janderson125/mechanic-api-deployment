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
