#!/usr/bin/python3
"""
starts a Flask web application:

-Your web application must be listening on 0.0.0.0, port 5000
-You must use storage for fetching data from the storage engine (FileStorage or DBStorage) => from models import storage and storage.all(...)
-To load all cities of a State:
     If your storage engine is DBStorage, you must use cities relationship
     Otherwise, use the public getter method cities
-After each request you must remove the current SQLAlchemy Session:
     Declare a method to handle @app.teardown_appcontext
     Call in this method storage.close()
-Routes:
        /cities_by_states: display a HTML page: (inside the tag BODY)
          H1 tag: “States”
          UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
             LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag: with the list of City objects linked to the State sorted by name (A->Z)
                LI tag: description of one City: <city.id>: <B><city.name></B>
-Import this 7-dump to have some data
-You must use the option strict_slashes=False in your route definition
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hello world for flask"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB for /hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_route(text):
    """display `C` followed by value of text variable
    replace underscores with a space"""
    return "C {:s}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_route(text="is cool"):
    """display `Python` followed by value of text variable
    replace underscores with a space"""
    return "Python {:s}".format(text.replace("_", " "))


@app.route('/number/<int:num>', strict_slashes=False)
def number_route(num):
    """display `n is a number` only if `n` is an int"""
    return "{:d} is a number".format(num)


@app.route('/number_template/<int:num>', strict_slashes=False)
def number_template(num):
    """displays a HTML page if `num` is an integer"""
    return render_template('5-number.html', num=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def number_odd_or_even(num):
    """displays a HTML page if `num` is an integer
    message on page changes depending on value passed"""
    return render_template('6-number_odd_or_even.html', num=num)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """displays a HTML page of state objects present in DBstorage
    message on page changes depending on value passed"""
    return render_template('7-states_list.html', states=storage.all("State"))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """displays a HTML page of city objects
    in a nested list of state objects present in DBstorage
    message on page changes depending on value passed"""
    return render_template(
        '8-cities_by_state.html', states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == "__main__":
 app.run(host="0.0.0.0", port="5000")
