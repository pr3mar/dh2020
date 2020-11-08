import json

from bitcoincli import Bitcoin


def write_data(data):
    str_data = json.dumps(data)
    print(f"dumped: {str_data}")
    str_data = f"{str_data}".encode('utf-8').hex()
    print(f"hex data = {str_data}")

    raw = bitcoin.createrawtransaction([], {"data": str_data})
    print(f"raws = {raw}")

    funded = bitcoin.fundrawtransaction(raw)
    print(f"funded = {funded}")

    signed = bitcoin.signrawtransaction(funded['hex'])
    print(f"signed = {signed}")

    balance = bitcoin.getbalance()
    print(f"balance = {balance}")

    sent_tx = bitcoin.sendrawtransaction(signed['hex'])
    print(f"sent tx = {sent_tx}")

    decoded = bitcoin.decoderawtransaction(signed['hex'])
    print(f"decoded = {decoded}")
    return sent_tx


if __name__ == '__main__':
    bitcoin = Bitcoin('user', 'password', '127.0.0.1', '18332')
    info = bitcoin.getblockchaininfo()
    print(info)

    block_count = bitcoin.getblockcount()
    print(block_count)

    tx = write_data({"data": "new_some", "hello": "World"})
    print(tx)
