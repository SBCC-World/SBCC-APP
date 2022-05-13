from web3 import Web3
import json

token_from = ""
private_key = ""

web3_BSC = Web3(Web3.HTTPProvider(""))
sbcc_contract = '0x6e02Be885FcA1138038420fDdD4B41C59a8Cea6D'

with open("abi.json") as f:
    abi = json.load(f)


def send_token(amount, to):
    try:
        bep20_contract = web3_BSC.toChecksumAddress(sbcc_contract)
        contract_bsc = web3_BSC.eth.contract(address=bep20_contract, abi=abi)
        bsc_Nonce = web3_BSC.eth.getTransactionCount(token_from)
        contract_method_transferToken = contract_bsc.functions.transfer(web3_BSC.toChecksumAddress(to), web3_BSC.toWei(amount, 'ether'))
        contract_method_transfer_build_tx = contract_method_transferToken.buildTransaction({
          'chainId': 56,
          'nonce': bsc_Nonce,
          'from': web3_BSC.toChecksumAddress(token_from),
          'gas': 210000,
          'gasPrice': web3_BSC.toWei('5', 'gwei'),
        })
        bsc_sign_tx_transferToken = web3_BSC.eth.account.signTransaction(contract_method_transfer_build_tx, private_key)
        bscTxHash = web3_BSC.eth.sendRawTransaction(bsc_sign_tx_transferToken.rawTransaction)
    except Exception as e:
        print(e)

