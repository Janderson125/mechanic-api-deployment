from flask import Blueprint, jsonify
from app import models

tickets_bp = Blueprint("tickets", __name__)

@tickets_bp.route("/", methods=["GET"])
def get_tickets():
    return jsonify(models.tickets)

@tickets_bp.route("/<int:ticket_id>", methods=["GET"])
def get_ticket(ticket_id):
    ticket = next((t for t in models.tickets if t["id"] == ticket_id), None)
    if ticket:
        return jsonify(ticket)
    return jsonify({"error": "Ticket not found"}), 404
