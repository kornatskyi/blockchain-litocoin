"""
Imports
"""

import requests
from flask import Flask, request
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

    @app.route("/blockchain")
    def blockchain():
        return f"Current blockchain: {context.node.blockchain}"

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
