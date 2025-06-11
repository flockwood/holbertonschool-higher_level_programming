#!/usr/bin/python3
"""
Flask RESTful API for user management.
This script creates a simple API with endpoints for managing users.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route('/')
def home():
    """
    Root endpoint that returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    Returns a JSON list of all usernames stored in the API.
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def get_status():
    """
    Returns the API status.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the full object corresponding to the provided username.
    If user doesn't exist, returns an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Adds a new user to the users dictionary.
    Expects JSON data with username, name, age, and city.
    """
    data = request.get_json()
    
    # Check if username is provided
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    username = data['username']
    
    # Create user object
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    
    # Add user to storage
    users[username] = user
    
    # Return confirmation
    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()
