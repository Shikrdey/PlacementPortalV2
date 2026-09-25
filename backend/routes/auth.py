from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import db, User, Student, Recruiter
from flask_jwt_extended import create_access_token


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    existing_user = User.query.filter_by(email = data["email"]).first()
    if existing_user:
        return jsonify({"message":"User already exists"}), 409
    user = User(email = data["email"].strip(), password = generate_password_hash(data["password"].strip()), role = data["role"])
    db.session.add(user)
    db.session.commit()

    return jsonify({"message":"User registered successfully"}), 200


@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(email = data["email"]).first()
    if user:
        if check_password_hash(user.password, data["password"]):
            access_token = create_access_token(identity = str(user.id), additional_claims = {"role": user.role})
            return jsonify({
                "message":"Login Successful",
                "access_token": access_token,
                "role": user.role
                }), 200
        else:
            return jsonify({"message":"Invalid Password"}), 401
    return jsonify({"message":"User does not exist"}), 404