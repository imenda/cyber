import hashlib
import time

# Classe per rappresentare un blocco
class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + str(self.previous_hash) + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()

# Classe per rappresentare una blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Creazione di una blockchain con 4 blocchi
blockchain = Blockchain()
num_blocks_to_add = 4

for _ in range(num_blocks_to_add):
    data = f"Transazione nel blocco {_ + 1}"
    new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, int(time.time()), data)
    blockchain.add_block(new_block)
    print(f"Blocco #{new_block.index} aggiunto alla blockchain.")
    print(f"Hash del blocco: {new_block.hash}\n")

print("Blockchain completa.")
