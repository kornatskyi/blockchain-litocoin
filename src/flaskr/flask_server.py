"""
Imports
"""

import os
import requests
from flask import Flask, request, Response
from src.classes.Context import Context

from .node_routes import node_routes

def create_app(context: Context, test_config=None):
    """
    Create and configure the app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # for more details go here https://flask.palletsprojects.com/en/2.2.x/tutorial/factory/
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # ----- Register blueprints ----- #
    app.register_blueprint(blueprint=node_routes)

    # ----- Root level routes ----- #
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/trigger")
    def trigger():
        response = requests.get('http://localhost:5000/name', timeout=5)
        print("Response text:" + response.text)
        return f"Triggered node has name {response.text}"
    
    @app.route("/generate-block")
    def generate_block():
        node = context.node
        new_block = node.generate_block("New1 block")
        block_json = new_block.toJSON()
        node.get_blockchain().add_a_block(new_block)
        node.get_blockchain().write_blockchain_to_the_file()
        return Response(block_json)

    @app.route("/blockchain")
    def blockchain():
        message = ""
        failed = False
        try:
            context.node.get_blockchain().load_blockchain_from_the_file()
        except Exception as exception:
            failed = True
            message = exception.__str__()
        if failed:
            return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
        blockchain_json = [block.toJSON()
                           for block in context.node.get_blockchain().get_blocks()]
        return Response(blockchain_json) 

    @app.route("/load-blockchain")
    def load_blockchain():
        message = ""
        failed = False
        try:
            context.node.get_blockchain().load_blockchain_from_the_file()
        except Exception as exception:
            failed = True
            message = exception.__str__()
        if failed:
            return f"<h3 style=\"color:red\">Failed to load blockchain</h3><p>Error message:{message}</p>"
        return "<h3 style=\"color:green\">Blockchain loaded sucsesfully.</h3>"

    @app.route("/name")
    def get_node_name():
        print("hello")
        return f"{context.node.get_name()}"

    @app.route("/set/name")
    def set_node_name():
        new_name = request.args.get('name')
        context.node.set_name(new_name)
        return f"New name '{new_name}' succsesfully set"


    return app

