#!/usr/bin/python3
""" 2-c_route module """

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
