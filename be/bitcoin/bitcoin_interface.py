import json

from bitcoincli import Bitcoin

DEBUG = False


class BitcoinWrapper:
    def __init__(self):
        self.bitcoin = Bitcoin('user', 'password', '127.0.0.1', '18332')

    def write_data(self, data: dict) -> str:
        str_data = json.dumps(data)
        if DEBUG: print(f"dumped: {str_data}")
        str_data = f"{str_data}".encode('utf-8').hex()
        if DEBUG: print(f"hex stored_data = {str_data}")

        raw = self.bitcoin.createrawtransaction([], {"data": str_data})
        if DEBUG: print(f"raws = {raw}")

        funded = self.bitcoin.fundrawtransaction(raw)
        if DEBUG: print(f"funded = {funded}")

        signed = self.bitcoin.signrawtransaction(funded['hex'])
        if DEBUG: print(f"signed = {signed}")

        balance = self.bitcoin.getbalance()
        if DEBUG: print(f"balance = {balance}")

        sent_tx = self.bitcoin.sendrawtransaction(signed['hex'])
        print(f"stored tx_id = {sent_tx}")

        return sent_tx

    def retrieve_data(self, tx: str) -> dict:
        raw_data = self.bitcoin.getrawtransaction(tx)
        decoded_data = self.bitcoin.decoderawtransaction(raw_data)
        if DEBUG: print(f"{json.dumps(decoded_data, indent=4)}")
        data = [x["scriptPubKey"]["asm"].split(' ')[2] for x in decoded_data["vout"] if "OP_RETURN" in x["scriptPubKey"]["asm"]][0]
        return json.loads(bytes.fromhex(data).decode('utf-8'))


if __name__ == '__main__':
    # bitcoin = Bitcoin('user', 'password', '127.0.0.1', '18332')

    # info = bitcoin.getblockchaininfo()
    # print(info)

    # block_count = bitcoin.getblockcount()
    # print(block_count)

    bitcoinWrapper = BitcoinWrapper()

    tx_id = bitcoinWrapper.write_data({"stored_data": "new_some", "hello": "World"})

    stored_data = bitcoinWrapper.retrieve_data(tx_id)
    print(stored_data)

