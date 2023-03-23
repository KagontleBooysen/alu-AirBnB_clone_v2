#!/usr/bin/python3
""" A script that starts a Flask web application and do some dummy stuff
Returns:
    _type_: _description_
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False)
def python_is_cool(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    # start the flask app
    app.run(host='0.0.0.0', port=5000, debug=True)

