# app/routes/tickets.py
from flask import Blueprint, request, jsonify
from app import db
from app.models import Ticket
from app.schemas import TicketSchema

tickets_bp = Blueprint('tickets', __name__)
ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)

@tickets_bp.route('/', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return tickets_schema.jsonify(tickets)

@tickets_bp.route('/<int:id>', methods=['GET'])
def get_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    return ticket_schema.jsonify(ticket)

@tickets_bp.route('/', methods=['POST'])
def create_ticket():
    data = request.get_json()
    new_ticket = ticket_schema.load(data)
    db.session.add(new_ticket)
    db.session.commit()
    return ticket_schema.jsonify(new_ticket), 201

@tickets_bp.route('/<int:id>', methods=['PUT'])
def update_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(ticket, key, value)
    db.session.commit()
    return ticket_schema.jsonify(ticket)

@tickets_bp.route('/<int:id>', methods=['DELETE'])
def delete_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    return '', 204
