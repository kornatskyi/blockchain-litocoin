from flask import Blueprint


info_routes = Blueprint('info', __name__, url_prefix="/info")

@info_routes.route("/route")
def info_example():
    return "<h1>This is example of an info endpoint</h1>"

