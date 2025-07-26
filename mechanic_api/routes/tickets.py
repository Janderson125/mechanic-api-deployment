from flask import Blueprint, request, jsonify
from mechanic_api.app import db, models
from mechanic_api.app.schemas import TicketSchema

tickets_bp = Blueprint("tickets", __name__)

@tickets_bp.route("/", methods=["GET"])
def get_tickets():
    tickets = models.Ticket.query.all()
    schema = TicketSchema(many=True)
    return jsonify(schema.dump(tickets))

@tickets_bp.route("/", methods=["POST"])
def create_ticket():
    data = request.get_json()
    schema = TicketSchema()
    ticket = schema.load(data, session=db.session)
    db.session.add(ticket)
    db.session.commit()
    return schema.jsonify(ticket), 201
