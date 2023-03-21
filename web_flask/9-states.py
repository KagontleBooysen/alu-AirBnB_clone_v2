#!/usr/bin/python3
"""
-Your web application must be listening on 0.0.0.0, port 5000
-Routes:
        /cities_by_states: display a HTML page: (inside the tag BODY)
         -H1 tag: “States”
         -UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
         -LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
        -LI tag: description of one City: <city.id>: <B><city.name></B>
-Import this 7-dump to have some data
-You must use the option strict_slashes=False in your route definition
"""

# Import necessary modules
from flask import Flask, render_template
from models import storage

# Create Flask app
app = Flask(__name__)

# Declare method to close SQLAlchemy session after each request
@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# Define /states route
@app.route('/states', strict_slashes=False)
def list_states():
    # Fetch all State objects from storage
    states = storage.all("State").values()

    # Sort states by name
    states = sorted(states, key=lambda x: x.name)

    # Render HTML template with list of states
    return render_template('states.html', states=states)

# Define /states/<id> route
@app.route('/states/<id>', strict_slashes=False)
def show_state(id):
    # Fetch State object with given ID from storage
    state = storage.get("State", id)

    # If state is found, fetch associated cities and sort by name
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)

        # Render HTML template with state and cities information
        return render_template('state.html', state=state, cities=cities)
    else:
        # If state is not found, render HTML template with "Not found!" message
        return render_template('not_found.html')

# Run app on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

