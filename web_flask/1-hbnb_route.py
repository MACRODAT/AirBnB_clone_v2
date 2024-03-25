#!/usr/bin/python3
"""
web framework project
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns default message"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def index():
    """returns default message"""
    return "hbnb"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
