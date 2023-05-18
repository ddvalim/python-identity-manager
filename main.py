from flask import Flask, request, jsonify
from did import generate_did
import asyncio

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/did',methods=['GET'])
def create_did():
    seed = 'DPiLYqFDnl+UKdYTN5Wwg0/OqAVtqOfq'
    did, verkey = generate_did.generate_did(seed)
    return did, verkey