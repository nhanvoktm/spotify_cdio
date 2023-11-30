import web3
from web3 import Web3

w3 = Web3(web3.HTTPProvider('HTTP://127.0.0.1:7545'))

w3.is_connected()

w3.eth.get_block('latest')

# print(w3.eth.accounts[2])

print(w3.eth.get_balance('0xDeF633b5b234cd64aA21d58F7B502C9A248EBaF8'))

# print(w3.eth.accounts)

print(w3.eth.get_proof('0xDeF633b5b234cd64aA21d58F7B502C9A248EBaF8' ,[0]))