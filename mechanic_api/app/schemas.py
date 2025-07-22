from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Mechanic, Ticket
from app import db

ma = Marshmallow()

class MechanicSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Mechanic
        sqla_session = db.session
        load_instance = True

class TicketSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        sqla_session = db.session
        load_instance = True
