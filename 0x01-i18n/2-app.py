#!/usr/bin/env python3
"""Instantiating the babel app"""
from urllib import request
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """The configuration of the app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """Welcome HTML page"""
    return render_template('2-index.html')


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match language according suppported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
