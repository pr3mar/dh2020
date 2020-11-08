import pandas as pd
import pickle
import json
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/api/hello')
@cross_origin()
def hello_world():
    return 'Hello, World!'


@app.route('/api/spills')
def get_spills():
    return pd.read_csv('data/spills.csv').to_json(orient='records')


@app.route('/api/aggregated/<spill_id>', methods=['GET'])
def get_trades(spill_id):
    analysis = []
    with open('../data/analysis_data.pkl', "rb") as f:
        analysis = pickle.load(f)
    return json.dumps(analysis[spill_id], sort_keys=True)

@app.route('/api/sentiment/<spill_id>', methods=['GET'])
def get_trades(spill_id):
    analysis = []
    with open('../data/sentiment_data.pkl', "rb") as f:
        analysis = pickle.load(f)
    return json.dumps(analysis[spill_id], sort_keys=True)

