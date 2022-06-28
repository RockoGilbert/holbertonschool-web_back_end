#!/usr/bin/env python3
"""A flask app that has a single GET route"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


# Authentication
AUTH = Auth()


# Flask App
app = Flask(__name__)


@app.route('/', methods=['GET'], stict_slashes=False)
def index():
    """Route handler"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def create():
    """Creates an email if the user doesn't exist"""

    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.create_users(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
