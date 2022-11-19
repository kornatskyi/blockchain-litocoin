from pathlib import Path
import sys
import getopt
from src.classes import Context, Node
from src.flask_server import start_flask_sever


def main(argv):
    """
    Main method
    """

    env_file = ''
    
    try:
        (opts, _) = getopt.getopt(argv, "he:", ["efile="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -e nodeDefault.json')
            sys.exit()
        elif opt in ("-e", "--env"):
            env_file = arg
        else:
            env_file = './config_files/nodeDefault.json'

    print(sys.argv)

    current_node = Node(Path(env_file))

    # Create context
    context = Context(node=current_node)

    # starting Flask web server
    start_flask_sever(context=context, port=current_node.port, debug=True)


if __name__ == "__main__":
    # Clearing the sonsole
    # os.system('clear')
    main(sys.argv[1:])
