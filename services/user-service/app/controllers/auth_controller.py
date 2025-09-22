# services/user-service/app/controllers/auth_controller.py

from app.services.auth_service import AuthService
from app.services.user_service import UserService
from flask import Blueprint, jsonify, request

auth_blueprint = Blueprint("auth", __name__)
user_service = UserService()
auth_service = AuthService()


@auth_blueprint.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or not all(
        k in data for k in ("username", "email", "password", "fullName")
    ):
        return jsonify({"message": "Missing required fields"}), 400

    new_user = user_service.register_new_user(data)

    if not new_user:
        return jsonify({"message": "Username or email already exists"}), 409

    return jsonify({"message": "User registered successfully"}), 201


@auth_blueprint.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "Missing username or password"}), 400

    user = auth_service.authenticate(data["username"], data["password"])

    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    token = auth_service.generate_token(user)
    return jsonify({"accessToken": token})
