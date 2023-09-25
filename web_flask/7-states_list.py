from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    state_info_list = [{"state_id": state.id, "state_name": state.name} for state in states]
    return render_template("7-states_list.html", state_info_list=state_info_list)


@app.teardown_appcontext
def close_session(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
