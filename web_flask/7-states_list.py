#!/usr/bin/python3
"""starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State
# from models.engine.db_storage import close

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays a HTML page with a list of states """
    states = sorted(list(storage.all(State).values()),
                    key=lambda state: state.name)
    # print(states)
    return render_template('7-states_list.html', states=states)

# Close the session after each request


@app.teardown_appcontext
def close_session(exception):
    """ Closes the session after each request """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
