
from web3 import Web3

import json

w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))

sender = w3.eth.accounts[0]

recipient = w3.eth.accounts[1]

print(sender)

e = w3.to_wei(5,"ether")

e3=w3.eth.send_transaction({
    "from":sender,
    "to":"0x550A64B9bf76C8e0ba46fc5Fdfa947ac1aA4F73D",
    "value":e
})

address = w3.to_checksum_address("0x550A64B9bf76C8e0ba46fc5Fdfa947ac1aA4F73D")
abi = json .loads('[{"inputs":[{"internalType":"int256","name":"a1","type":"int256"},{"internalType":"int256","name":"b1","type":"int256"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"a","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"b","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"x","outputs":[{"internalType":"int256","name":"","type":"int256"}],"stateMutability":"view","type":"function"}]')
contract1 = w3.eth.contract(address=address,abi=abi)

nonce = w3.eth.get_transaction_count(sender)

print(w3.eth.gas_price)

tx = contract1.functions.transfer(recipient,w3.to_wei())



tx_hash = w3.eth.send_raw_transaction()