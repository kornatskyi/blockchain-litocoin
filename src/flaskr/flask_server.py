"""
Imports
"""
import os
from flask import Flask
from .node_routes import node_routes
from .info import info_routes
from .action import action_routes

def create_app(test_config=None):
    """
    Create and configure the Flask app
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
    app.register_blueprint(blueprint=info_routes)
    app.register_blueprint(blueprint=action_routes)

    # ----- Root level routes ----- #
    @app.route('/')
    def default():
        return 'online'

    @app.route('/hello')
    def hello():
        return 'Hello, World!'



    return app

