# Todo:

1. Generate new block



# Blockchain workflow


# User prespectvie

## What user can do

- Run a node ✔
- Scan network for other peers
- Request blockchain from other peers
  - node returns its blockchain ✔
- Main a block
  - main a block ✔
  - add block to the blockchain ✔
- Propagate mained blocks among peers
- Listen for mained blocks
- Create "transaction"
- List all transactions in a network
- Rules for blockchain validation


### How to discover peers?
There should be hardcoded peers address to discover at least some peers on the first run
After that, node can maintain it's own list of peers, and connect to them each time it needs
Each node will share it's list of peers with other nodes

### How to download blockchain from other peers? 
Send the hash of a last block you have (genesis block it it's firs time download)
The peer will validate and will send back a block it has after the hash you sent
And actually the peer can send back more than 1 block
