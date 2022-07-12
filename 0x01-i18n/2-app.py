#!/usr/bin/env python3
"""Module for 2-app.py"""
from flask import Flask, render_template, request
from flask import Babel

app = Flask(__name__)
babel = Babel(app)