#!/usr/bin/python3
"""
Flask API with Basic and JWT Authentication.
This script implements security features for API endpoints.
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-string'

# Initialize authentication extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data with hashed passwords and roles
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


@auth.verify_password
def verify_password(username, password):
    """
    Verify password for basic authentication.
    """
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None


@auth.error_handler
def auth_error(status):
    """
    Handle basic authentication errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Protected route requiring basic authentication.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Login endpoint that returns JWT token for valid credentials.
    """
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400
    
    username = data['username']
    password = data['password']
    
    if username in users and check_password_hash(users[username]['password'], password):
        # Create token with user identity and role
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]}
        )
        return jsonify({"access_token": access_token})
    
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Protected route requiring JWT authentication.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    Protected route requiring JWT authentication and admin role.
    """
    current_user = get_jwt_identity()
    
    if current_user not in users:
        return jsonify({"error": "Invalid user"}), 401
    
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    
    return "Admin Access: Granted"


# JWT Error Handlers
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
    app.run(debug=True)
