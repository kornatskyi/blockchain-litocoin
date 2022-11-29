from flask import Blueprint


actions_routes = Blueprint('action', __name__, url_prefix="/action")

@actions_routes.route("/route")
def action_example():
    return "<h1>This is example of an action endpoint</h1>"