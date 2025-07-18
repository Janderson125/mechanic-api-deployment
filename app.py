from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Configure your database URI here
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:Austin78702!@localhost/ecommerce_api"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"

# Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# Initialize the database inside app context
with app.app_context():
    db.create_all()

# Routes
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the E-Commerce API!"})

@app.route("/users", methods=["POST"])
def add_user():
    name = request.json.get("name")
    address = request.json.get("address")
    email = request.json.get("email")

    if not name or not address or not email:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if user with email already exists to prevent duplicates
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "User with this email already exists"}), 409

    new_user = User(name=name, address=address, email=email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user), 201

@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    return users_schema.jsonify(all_users)

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)

    name = request.json.get("name", user.name)
    address = request.json.get("address", user.address)
    email = request.json.get("email", user.email)

    # Check if updating email to one that already exists on another user
    if email != user.email:
        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already in use"}), 409

    user.name = name
    user.address = address
    user.email = email

    db.session.commit()
    return user_schema.jsonify(user)

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
