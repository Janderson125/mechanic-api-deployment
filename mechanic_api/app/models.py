from mechanic_api.app import db

class Mechanic(db.Model):
    __tablename__ = 'mechanics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=True)

class Ticket(db.Model):
    __tablename__ = 'tickets'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanics.id'))
    mechanic = db.relationship('Mechanic', backref=db.backref('tickets', lazy=True))
