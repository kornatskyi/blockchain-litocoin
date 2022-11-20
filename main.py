import json
from pathlib import Path
import sys
import getopt
from src.classes.Block import Block
from src.classes.BlockChain import BlockChain
from src.classes.Context import Context
from src.classes.Node import Node, generate_block
from src.constants import REPO_PATH
from src.flask_server import start_flask_sever

# blockchain = BlockChain(Path(REPO_PATH) / "blockchain/blockchain.json")

# blockchain.load_blockchain_from_file()

# blockchain.validate_blockchain()

# genesis_block = Block("genesis block", "5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9", 0, 0)

# new_block = generate_block(genesis_block,"new block data", 2)
# print(new_block.toJSON())


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
    # Create a current node
    current_node = Node(Path(REPO_PATH) / config_dir)

    # Create context
    context = Context(node=current_node)

    # starting Flask web server
    start_flask_sever(context=context, port=current_node.port, debug=True)


if __name__ == "__main__":
    # Clearing the sonsole
    # os.system('clear')
    main(sys.argv[1:])
