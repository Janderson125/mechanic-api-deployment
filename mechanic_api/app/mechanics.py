from flask import Blueprint, request, jsonify
from mechanic_api.app import db, models
from mechanic_api.app.schemas import MechanicSchema

mechanics_bp = Blueprint("mechanics", __name__)

@mechanics_bp.route("/", methods=["GET"])
def get_mechanics():
    mechanics = models.Mechanic.query.all()
    schema = MechanicSchema(many=True)
    return jsonify(schema.dump(mechanics))

@mechanics_bp.route("/", methods=["POST"])
def create_mechanic():
    data = request.get_json()
    schema = MechanicSchema()
    mechanic = schema.load(data, session=db.session)
    db.session.add(mechanic)
    db.session.commit()
    return schema.jsonify(mechanic), 201
