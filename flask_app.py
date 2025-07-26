from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

# Load config based on environment or default to development
env = os.getenv('FLASK_ENV', 'development')
if env == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Example model
class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

# Example schema
class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic

mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)

@app.route('/')
def home():
    return "Hello, Mechanic API!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if not exist
    app.run()
