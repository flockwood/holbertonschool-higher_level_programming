#!/usr/bin/env python3

"""
Flask API with Basic Authentication and JWT Authentication.

This API implements:
- Basic authentication using Flask-HTTPAuth.
- JWT-based authentication with Flask-JWT-Extended.
- Role-based access control for admin-only routes.
- Custom error handlers for JWT-related issues.

Endpoints:
- /basic-protected: Protected with Basic Authentication.
- /login: Generates a JWT token upon valid login.
- /jwt-protected: Requires a valid JWT token.
- /admin-only: Restricted to admin users only.

Author: Your Name
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

# In-memory user database
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin123"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify user credentials using Basic Authentication.

    Args:
        username (str): The provided username.
        password (str): The provided password.

    Returns:
        str or None: The username if authentication succeeds, else None.
    """
    if username in users and check_password_hash(
            users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Protected route using Basic Authentication.

    Returns:
        JSON response with an access granted message.
    """
    return jsonify({"message": "Basic Auth: Access Granted"})


@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint that generates a JWT token upon valid authentication.

    Request JSON:
    {
        "username": "user1",
        "password": "password"
    }

    Returns:
        JSON response with the generated JWT token or an error message.
    """
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(
            users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT Token
    user_data = {"username": username, "role": users[username]["role"]}
    access_token = create_access_token(
        identity=username, additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Protected route that requires a valid JWT token.

    Returns:
        JSON response with access granted and the user's identity.
    """
    user = get_jwt_identity()
    return jsonify({"message": "JWT Auth: Access Granted", "user": user})


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only protected route that requires a valid JWT token.

    Returns:
        JSON response with an access granted message if the user is admin.
        Otherwise, a 403 error message is returned.
    """
    claims = get_jwt()
    role = claims.get("role", "unknown")

    if role != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"})


# Custom JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handles unauthorized access due to missing or invalid JWT token.

    Args:
        err (str): Error message.

    Returns:
        JSON response with a 401 Unauthorized status.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handles invalid JWT token errors.

    Args:
        err (str): Error message.

    Returns:
        JSON response with a 401 Unauthorized status.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handles expired JWT token errors.

    Args:
        err (str): Error message.

    Returns:
        JSON response with a 401 Unauthorized status.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handles revoked JWT token errors.

    Args:
        err (str): Error message.

    Returns:
        JSON response with a 401 Unauthorized status.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handles requests that require a fresh token but receive a non-fresh one.

    Args:
        err (str): Error message.

    Returns:
        JSON response with a 401 Unauthorized status.
    """
    return jsonify({"error": "Fresh token required"}), 401


@auth.error_handler
def unauthorized():
    """Return JSON response for unauthorized access."""
    return jsonify({"error": "Unauthorized Access"}), 401


# 🚀 Run the Flask App
if __name__ == "__main__":
    app.run(debug=True)
