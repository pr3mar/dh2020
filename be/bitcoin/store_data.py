import pandas as pd
import json
from be.bitcoin.bitcoin_interface import BitcoinWrapper


if __name__ == '__main__':
    tx_ids = []
    bitcoinWrapper = BitcoinWrapper()
    data = pd.read_csv("data/spills.csv")
    json_data = json.loads(data.to_json(orient='records'))

    for i, record in enumerate(json_data):
        print(i, json.dumps(record))
        tx_id = bitcoinWrapper.write_data(record)
        tx_ids.append(tx_id)
    print(tx_ids)
    data['bitcoin_tx'] = tx_ids
    data.to_csv("data/spills_tx.csv", index=None)
