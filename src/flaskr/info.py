from flask import Blueprint, Response
from src.classes import Node


info_routes = Blueprint('info', __name__, url_prefix="/info")

@info_routes.route("/route")
def info_example():
    return "<h1>This is example of an info endpoint</h1>"

@info_routes.route("/blockchain")
def blockchain():
    message = ""
    failed = False
    node = Node()
    try:
        node.get_blockchain().load_blockchain_from_the_file()
    except Exception as exception:
        failed = True
        message = str(exception)
    if failed:
        return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
    blockchain_json = [block.toJSON()
                        for block in node.get_blockchain().get_blocks()]
    return Response(blockchain_json) 
