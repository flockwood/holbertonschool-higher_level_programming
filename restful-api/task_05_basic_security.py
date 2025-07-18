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


# JWT Error Handlers - Specific handlers for different JWT error types
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid token errors.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token errors.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token errors.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token errors.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle fresh token required errors.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
