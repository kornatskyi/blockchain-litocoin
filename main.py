from pathlib import Path
import sys
from src.classes.Node import Node
from src.constants import REPO_PATH
from src.flaskr.flask_server import create_app
import argparse


def main(args):
    """
    Main method
    """
    parser = argparse.ArgumentParser(description="Run a Litocoin node.")

    parser.add_argument(
        "-c",
        "--config",
        type=str,
        default="config_files/nodeDefault/",
        help="Path to the node's folder with configurations.",
    )
    parser.add_argument(
        "--port",
        type=int,
        help="The port on which to run the node (overrides config value).",
    )

    parsed_args = parser.parse_args(args)

    # Initialise singleton instance of a node
    current_node = Node(Path(REPO_PATH) / parsed_args.config)

    # If a port is provided via the command line, update the current_node's port
    if parsed_args.port:
        current_node.set_port = parsed_args.port

    # starting Flask web server
    # start_flask_sever(context=context, port=current_node._port, debug=True)
    app = create_app()

    print(f"Flask server is running on port {current_node.port}")
    app.run(port=current_node.port, debug=True)


if __name__ == "__main__":
    # Clearing the sonsole
    # os.system('clear')
    main(sys.argv[1:])
