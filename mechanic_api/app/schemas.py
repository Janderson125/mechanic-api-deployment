# app/schemas.py
from app import ma
from app.models import Mechanic, Ticket

class MechanicSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Mechanic
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    specialty = ma.auto_field()

class TicketSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ticket
        load_instance = True

    id = ma.auto_field()
    description = ma.auto_field()
    is_complete = ma.auto_field()
    mechanic_id = ma.auto_field()
