from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:8545'))
w3.eth.default_account = w3.eth.accounts[0]
address = w3.to_checksum_address("0x818278e3eee769C309653b741B01a48eD5b348eB")
import json
abi = json.loads('[{"inputs":[{"internalType":"int256","name":"a1","type":"int256"},{"internalType":"int256","name":"b1","type":"int256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"a","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"b","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"x","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"}]')
contract = w3.eth.contract(address=address,abi=abi)
tx = contract.functions.plus_2_number().transact()
print(tx)
import random
i = 10
while True:
    i = random.randint(5,25)
    tx = contract.functions.plus_2_number().transact()
    break
receipt = w3.eth.get_transaction_receipt(tx)
print(receipt)