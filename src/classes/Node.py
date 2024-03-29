# Standard libs
import json
from pathlib import Path
import urllib.parse
# Third party libs
import requests

from src.classes.Enums import PeerStatus

# My imports
from src.classes.Singleton import Singleton
from src.classes.Block import Block
from src.classes.BlockChain import BlockChain
from src.constants import REPO_PATH
from src.rules import NUMBER_OF_LEADING_ZEROS
from src.utils.cryptography import sha256


class Node(metaclass=Singleton):
    """
    Represents a node in a blockchain network.
    Node is a singleton instance because there could be only one Node for a running server
    """

    def __init__(self, config_dir_path: Path = None):
        # Path to configuration file with persistent information
        self._config_file_path = Path(config_dir_path) / "config.json"
        assert self._config_file_path.exists(
        ), f"No config file in a directory {config_dir_path}"
        jsondata = self._config_file_path.read_text()

        # Nodes name
        self._name = json.loads(jsondata)["name"]
        # Port on which node's flask server will be running
        self._port = json.loads(jsondata)["port"]
        # Peers URIs know to the node
        self._known_peers = json.loads(jsondata)["known_peers"]
        # Set of online peers
        self._online_peers = set[str]()
        # Availability status of a node to a network
        self._status = PeerStatus.ONLINE
        # Path to the file with persisted blockchain data
        self._blockchain_file_path = Path(
            REPO_PATH) / config_dir_path.__str__() / "blockchain.json"

        assert self._blockchain_file_path.exists(
        ), f"No blockchain file in {self._blockchain_file_path.__str__()}"

        # Dynamic(stored in memory(RAM)) blockchain
        self._blockchain = BlockChain(self._blockchain_file_path)
        # Load blockchain
        self._blockchain.load_blockchain_from_the_file()

    def set_name(self, new_name: str) -> None:
        """
        Name setter
        """
        self._name = new_name

    def get_name(self) -> str:
        """
        Get nodes name
        """
        return self._name

    def get_status(self) -> PeerStatus:
        """
        Node status getter
        """
        return self._status

    @property
    def port(self) -> int:
        """
        Get a port for this node's server 
        """
        return self._port

    @port.setter
    def port(self, new_port: int) -> None:
        """
        Set a port for this node's server
        """
        self._port = new_port

    def get_blockchain(self):
        """
        Returns blockchain to which this node refers to
        """
        return self._blockchain

    def generate_block(self, block_data: str) -> Block:
        """
        Node generates new block
        """
        new_block = generate_block(
            self._blockchain.get_last_block(), block_data, NUMBER_OF_LEADING_ZEROS)
        return new_block

    def check_peers_status(self) -> dict[str, PeerStatus]:
        """
        Return status of known peers
        """
        peers_status = dict[str, PeerStatus]()
        for peer_url in self._known_peers:
            try:
                # Send request to the know peer URI, to know it's status
                response = requests.get(urllib.parse.urljoin(
                    peer_url, "info/status"), timeout=3)
                if response.status_code >= 200 and response.status_code < 300:
                    peers_status[peer_url] = PeerStatus.ONLINE
                else:
                    peers_status[peer_url] = PeerStatus.OFFLINE
            except requests.exceptions.ConnectionError:
                peers_status[peer_url] = PeerStatus.OFFLINE
            except requests.exceptions.HTTPError:
                peers_status[peer_url] = PeerStatus.WRONG_RESPONSE
        return peers_status

    def update_online_peers(self) -> None:
        """
        Check what peers are online, and updates set of online peers 
        """
        peers_by_status = self.check_peers_status()
        for (peer, status) in peers_by_status.items():
            if status == PeerStatus.ONLINE:
                self._online_peers.add(peer)
            else:
                self._online_peers.pop(peer)

    def update_blockchain(self):
        """
        Updates blockchain by requesting most recent blocks from the known peers
        """
        blockchain_json: BlockChain
        self.update_online_peers()
        for peer_url in self._online_peers:
            json_l = requests.get(urllib.parse.urljoin(
                peer_url, "info/blockchain"), timeout=3).text
            if len(json.loads(json_l)) > len(self._blockchain.get_blocks()):
                blockchain_json = json_l

        if len(json.loads(blockchain_json)) > len(self._blockchain.get_blocks()):
            self._blockchain.load_blockchain_from_the_json(blockchain_json)


def generate_block(prev_block: Block, new_block_data: str, number_of_leading_zeros: int) -> Block:
    """
    Generate new block with special hash, which has leading zeros
    BLOCK DATA ORDER for hashing:
    (everything is string type)
    0. Previous block hash
    1. New block data(message)
    2. New height in string format
    3. New nonce
    """
    block_height = prev_block.height + 1
    block_data = prev_block.block_hash + new_block_data + str(block_height)
    new_hash = ''
    nonce = 0
    while new_hash[:number_of_leading_zeros] != ("0" * number_of_leading_zeros):
        nonce = nonce + 1
        new_hash = sha256(block_data + str(nonce))
    return Block(new_block_data, new_hash, nonce, block_height)
