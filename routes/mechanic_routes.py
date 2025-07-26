# routes/mechanic_routes.py
from flask import Blueprint, request, jsonify
from models import Mechanic, db

mechanic_bp = Blueprint('mechanic_bp', __name__)

@mechanic_bp.route('/', methods=['GET'])
def get_mechanics():
    mechanics = Mechanic.query.all()
    return jsonify([{ 'id': m.id, 'name': m.name, 'specialty': m.specialty } for m in mechanics])

@mechanic_bp.route('/', methods=['POST'])
def add_mechanic():
    data = request.get_json()
    new_mechanic = Mechanic(name=data['name'], specialty=data['specialty'])
    db.session.add(new_mechanic)
    db.session.commit()
    return jsonify({'message': 'Mechanic added successfully'}), 201

@mechanic_bp.route('/<int:mechanic_id>', methods=['PUT'])
def update_mechanic(mechanic_id):
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    data = request.get_json()
    mechanic.name = data.get('name', mechanic.name)
    mechanic.specialty = data.get('specialty', mechanic.specialty)
    db.session.commit()
    return jsonify({'message': 'Mechanic updated successfully'})

@mechanic_bp.route('/<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({'message': 'Mechanic deleted successfully'})
