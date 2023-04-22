
from flask import Blueprint


node_routes = Blueprint('node_ruotes', __name__, url_prefix="/node")

@node_routes.route("/route")
def node_route():
    """Node route

    Returns:
        html: HTML placeholder, not imp
    """
    return "<h1>Hello from node route. This rout isn't implemented yet</h1>☹️"