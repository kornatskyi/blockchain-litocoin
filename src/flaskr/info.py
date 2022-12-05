import json
from flask import Blueprint, Response
from src.classes import Node
from src.classes.Enums import PeerStatus


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

@info_routes.route("/status")
def status():
    node = Node()
    if node.get_status() == PeerStatus.ONLINE:
        return Response(status=200)
    else:
        return Response(status=503)

@info_routes.route("/peers-status")
def peers_status():
    """
    Get status of known peers
    """
    node = Node()
    peers_status_local = node.check_peers_status()
    print(peers_status_local)
    return Response(json.dumps(peers_status_local))