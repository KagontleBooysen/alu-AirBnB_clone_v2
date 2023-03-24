#!/usr/bin/python3
""" A script that starts a Flask web application and do some dummy stuff
Returns:
    _type_: _description_
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Displays a HTML page with a list of states """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def states_id(state_id):
    """ Displays a HTML page with a list of states """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    state_found = False
    for state in states:
        if state.id == state_id:
            state_found = True
            return render_template(
                '9-states.html',
                states=states,
                cities=state.cities,
                id=state_id)
    if not state_found:
        return render_template(
            '9-states.html',
            states=states,
            id=None)


@app.teardown_appcontext
def close_session(exception):
    """ Closes the session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
