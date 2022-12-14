from pathlib import Path
import sys
import getopt
from src.classes.Node import Node
from src.constants import REPO_PATH
from src.flaskr.flask_server import create_app

def main(argv):
    """
    Main method
    """
    config_dir = ''

    try:
        (opts, _) = getopt.getopt(argv, "hc:", ["config="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            sys.exit()
        elif opt in ("-c", "--config"):
            config_dir = arg
        else:
           raise Exception("Wrong command line arguments")

    # Initialise singleton instance of a node 
    current_node = Node(Path(REPO_PATH) / config_dir)
    

    # starting Flask web server
    # start_flask_sever(context=context, port=current_node._port, debug=True)
    app = create_app()

    print(f"Flask server is running on port {current_node.get_port()}")
    app.run(port=current_node.get_port(), debug=True)
    


if __name__ == "__main__":
    # Clearing the sonsole
    # os.system('clear')
    main(sys.argv[1:])
