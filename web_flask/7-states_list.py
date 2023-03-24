#!/usr/bin/python3
""" A flask server to return id and name of a State object
Returns:
    _type_: _description_
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Retrieve and sort the list of states from the database"""
    states = sorted(list(storage.all(State).values()), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the SQLAlchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


