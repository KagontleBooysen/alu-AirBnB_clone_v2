#!/usr/bin/python3
""" A script that starts a Flask web application and do some dummy stuff
Returns:
    _type_: _description_
"""

from flask import Flask, render_template

app = Flask(__name_)

@app.teardown_appcontext
def handle_teardow(self):
    """
    Después de cada solicitud, debe eliminar
    la sesión actual de SQLAlchemy
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_of_state():
    """
    Función llamada con la ruta /states_list
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
