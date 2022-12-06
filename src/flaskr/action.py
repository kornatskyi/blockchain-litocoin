from flask import Blueprint, Response
from src.classes import Node


action_routes = Blueprint('action', __name__, url_prefix="/action")


@action_routes.route("/generate-block")
def generate_block():
    """
    Make node to generate a block and write it to a blockchain file
    """
    node = Node()
    new_block = node.generate_block("New1 block")
    block_json = new_block.toJSON()
    node.get_blockchain().add_a_block(new_block)
    node.get_blockchain().write_blockchain_to_the_file()
    return Response(block_json)

@action_routes.route("/load-blockchain")
def load_blockchain():
    """
    Make a node to load a blockchain from a file
    """
    message = ""
    failed = False
    node = Node()
    try:
        node.get_blockchain().load_blockchain_from_the_file()
    except Exception as exception:
        failed = True
        message = exception.__str__()
    if failed:
        return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
    return "<h3 style=\"color:green\">Blockchain loaded successfully.</h3>"

@action_routes.route("update-blockchain")
def update_blockchain():
    """
    Updates blockchain by requesting most recent blocks from the known peers
    """
    node = Node()
    node.update_blockchain()
    return Response(node.get_blockchain())