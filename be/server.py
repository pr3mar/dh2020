import pandas as pd
import pickle
import json
from flask import Flask
from flask_cors import CORS, cross_origin
import random


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
def get_analysis(spill_id):
    analysis = []
    with open('../data/analysis_data.pkl', "rb") as f:
        analysis = pickle.load(f)
    if spill_id in analysis:
        return json.dumps(analysis[spill_id], sort_keys=True)
    else:
       return json.dumps(random.choice(list(analysis.values())), sort_keys=True)

@app.route('/api/sentiment/<spill_id>')
def get_sentiments(spill_id):
    analysis = []
    with open('../data/sentiments.pkl', "rb") as f:
        analysis = pickle.load(f)
    if spill_id in analysis:
        return json.dumps(analysis[spill_id], sort_keys=True)
    else:
        prepd = {'Angry': 0.2, 'Fear': 0.27, 'Happy': 0.03, 'Sad': 0.1, 'Surprise': 0.4}
        return json.dumps(prepd,sort_keys=True)
