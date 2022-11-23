"""
Imports
"""

import requests
from flask import Flask, request, Response
from src.classes.Context import Context


def start_flask_sever(context: Context, port: int, debug: bool):
    """
    Flask routs
    """

    # Create flas app
    app = Flask(__name__)

    @app.route("/trigger")
    def trigger():
        response = requests.get('http://localhost:5000/name', timeout=5)
        print("Response text:" + response.text)
        return f"Triggered node has name {response.text}"
    
    @app.route("/generate-block")
    def generate_block():
        new_block = context.node.generate_block("New1 block")
        block_json = new_block.toJSON()
        return Response(block_json)
        pass

    @app.route("/blockchain")
    def blockchain():
        message = ""
        failed = False
        try:
            context.node.blockchain.load_blockchain_from_file()
        except Exception as exception:
            failed = True
            message = exception.__str__()
        if failed:
            return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
        blockchain_json = [block.toJSON()
                           for block in context.node.blockchain.blocks]
        return Response(blockchain_json) 

    @app.route("/load-blockchain")
    def load_blockchain():
        message = ""
        failed = False
        try:
            context.node.blockchain.load_blockchain_from_file()
        except Exception as exception:
            failed = True
            message = exception.__str__()
        if failed:
            return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
        return "<h3 style=\"color:green\">Blockchain loaded sucsesfully.</h3>"

    @app.route("/name")
    def get_node_name():
        print("hello")
        return f"{context.node.name}"

    @app.route("/set/name")
    def set_node_name():
        new_name = request.args.get('name')
        context.node.set_name(new_name)
        return f"New name '{new_name}' succsesfully set"

    print(f"Flask server is running on port {port}")
    app.run(port=port, debug=debug)
