# Litocoin Node Project (In Development)

## Overview

Litocoin is a simple, decentralized cryptocurrency project built for educational purposes. The project consists of a network of nodes that communicate with each other to maintain a distributed ledger, known as the blockchain. The Litocoin nodes use a Proof-of-Work algorithm to validate and add new blocks to the blockchain, ensuring its security and integrity. Please note that this project is still in development.

## Features

- Node implementation with a Flask web server for communication between nodes
- Basic blockchain structure with the ability to add new blocks
- Proof-of-Work algorithm for block validation
- Singleton design pattern for the Node class
- Command line interface for running nodes with customizable configuration options
- Basic API for interacting with a node, including endpoints for generating blocks, updating the blockchain, and checking the status of peers
- Unit tests for core functionality

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Flask

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/litocoin.git
```

2. Navigate to the project folder:

```bash
cd litocoin
```

3. Install the required packages:

```python
pip install -r requirements.txt
```

### Running a Node

To run a Litocoin node, execute the `main.py` script with the desired command line arguments. For example:

```python
python main.py -c config_files/nodeDefault/
```

This command runs a node with the default configuration provided in the `config_files/nodeDefault/` directory.

## Usage

The Litocoin node exposes an API for interacting with its blockchain and other nodes. Some of the available endpoints include:

- `/` - Check if the node is online
- `/hello` - Test endpoint that returns "Hello, World!"
- `/action/generate-block` - Generate a new block and add it to the blockchain
- `/action/load-blockchain` - Load the blockchain from the persistent storage
- `/action/update-blockchain` - Update the blockchain by requesting the most recent blocks from known peers

## Contributing

Contributions are welcome!

## Future Improvements

- Implement a consensus algorithm to resolve conflicts between nodes
- Add support for transactions and a simple wallet
- Improve the API with additional endpoints and error handling
- Enhance security and performance
- Write more tests
