#!/usr/bin/python3
"""
Module: task_05_api_security
Demonstrates Basic Auth, JWT Auth, and Role-based access with Flask.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended.exceptions import JWTExtendedException
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "super-secret.key"

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

auth = HTTPBasicAuth()
jwt = JWTManager(app)


@auth.verify_password
def verify_password(username, password):
    """
    Checks is provided username and password match
    Returns the user dict if valid, else None.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


@auth.error_handler
def auth_error(status):
    """
    Handle basic authentication errors to return 401.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Example: curl -u user1:password http://127.0.0.1:5000/basic-protected
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Accepts JSON payload: {"username": "...", "password": "..."}
    Returns: {"access_token": "<JWT_TOKEN>"}
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = create_access_token(identity={
        "username": username, "role": user["role"]
    })
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Example: curl -H "Authorization: Bearer <TOKEN>"
    http://127.0.0.1:5000/jwt-protected
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Allows only admin users to access.
    """
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@app.errorhandler(JWTExtendedException)
def handle_jwt_errors(e):
    """
    Ensures all JWT errors returns 401 Unauthorized, as required.
    """
    return jsonify({"error": "Authentication error"}), 401


if __name__ == "__main__":
    app.run()
