import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-should-set-a-secret-key')  # fallback

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Austin78702!@localhost:3306/mydb"
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DEBUG = False
