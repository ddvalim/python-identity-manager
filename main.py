from flask import Flask, request, jsonify
from did import generate_did
from holder.anchor import AnchorHandle

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/did',methods=['GET'])
def create_did():
    seed = request.args.get('seed')
    did, verkey = generate_did.generate_did(seed)
    return jsonify(
        did=did,
        verkey=verkey
    )

@app.route('/seed',methods=['GET'])
def create_seed():
    anchor = AnchorHandle()
    return jsonify(**{
        "seed": anchor.generate_seed(),
        "key":anchor.generate_key(48)
    })