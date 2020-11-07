import pandas as pd
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
