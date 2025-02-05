#!/usr/bin/python3
""" 3-python_route module """

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ display “HBNB” """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def variable(text):
    """  display “C ” followed by the value of the text variable """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """  display “Python ” followed by the value of the text variable """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<n>", strict_slashes=False)
def number(n):
    if n.isnumeric():
        return f"{n} is a number"
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
