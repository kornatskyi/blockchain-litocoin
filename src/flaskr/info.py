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
    node = Node()
    blockchain_json = [block.toJSON()
                        for block in node.get_blockchain().get_blocks()]
    return Response(json.dumps(blockchain_json)) 

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