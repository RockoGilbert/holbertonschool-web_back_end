#!/usr/bin/env python3
"""A flask app that has a single GET route"""

from auth import Auth
from flask import Flask, jsonify, request, abort, redirect
from sqlalchemy.orm.exc import NoResultFound


# Authentication
AUTH = Auth()


# Flask App
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
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


@app.route('/reset_password', methods=["PUT"])
def update_password():
    """Route to update password"""

    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)

    {"email": "<user email>", "message": "Password updated"}, 200


@app.route('/login', methods=['POST'])
def login():
    """Route to log user into email"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
