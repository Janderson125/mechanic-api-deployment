from flask import Flask, request, jsonify
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

# Mechanic model
class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)

# Mechanic schema
class MechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic

mechanic_schema = MechanicSchema()
mechanics_schema = MechanicSchema(many=True)

@app.route('/')
def home():
    return "Hello, Mechanic API!"

@app.route('/mechanics', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return mechanics_schema.jsonify(mechanics)

@app.route('/mechanics', methods=['POST'])
def add_mechanic():
    name = request.json.get('name')
    specialty = request.json.get('specialty')
    if not name or not specialty:
        return jsonify({"error": "Missing name or specialty"}), 400
    new_mechanic = Mechanic(name=name, specialty=specialty)
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.jsonify(new_mechanic), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Insert example data if table is empty
        if Mechanic.query.count() == 0:
            example = Mechanic(name="Joe Smith", specialty="Engine Repair")
            db.session.add(example)
            db.session.commit()

    app.run(host='0.0.0.0', port=5000)
