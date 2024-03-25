#!/usr/bin/python3
"""
web framework project
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns default message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnbb():
    """returns default message"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def render(text):
    """returns default message"""
    return 'C ' + str(text).replace(' ', '_')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def render2(text="is cool"):
    """returns default message"""
    return 'Python ' + str(text).replace(' ', '_')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def rer(n):
    """display a HTML page for an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
