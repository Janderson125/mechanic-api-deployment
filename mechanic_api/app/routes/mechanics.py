from flask import Blueprint, jsonify
from mechanic_api.app import db, models
from mechanic_api.app.schemas import MechanicSchema

mechanics_bp = Blueprint("mechanics", __name__)

@mechanics_bp.route("/", methods=["GET"])
def get_mechanics():
    mechanics = models.Mechanic.query.all()
    schema = MechanicSchema(many=True)
    return jsonify(schema.dump(mechanics))

@mechanics_bp.route("/<int:mechanic_id>", methods=["GET"])
def get_mechanic(mechanic_id):
    mechanic = models.Mechanic.query.get(mechanic_id)
    if mechanic:
        schema = MechanicSchema()
        return jsonify(schema.dump(mechanic))
    return jsonify({"error": "Mechanic not found"}), 404
