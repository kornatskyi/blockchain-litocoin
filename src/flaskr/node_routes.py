
from flask import Blueprint


node_routes = Blueprint('node_ruotes', __name__, url_prefix="/node")

@node_routes.route("/route")
def node_route():
    return "<h1>Hello from node route</h1>"