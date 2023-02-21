from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["63f4e0ac953b9f76446901c5"]

@app.route('/collection', methods=['GET'])
def get_collection():
    collection = db["mycollection"]
    data = collection.find()
    return dumps(data)

@app.route('/collection/<id>', methods=['GET'])
def get_document(id):
    collection = db["mycollection"]
    data = collection.find_one({'_id': ObjectId(id)})
    return dumps(data)

@app.route('/collection', methods=['POST'])
def add_document():
    collection = db["mycollection"]
    data = request.json
    collection.insert_one(data)
    return jsonify({'status': 'success'})

@app.route('/collection/<id>', methods=['PUT'])
def update_document(id):
    collection = db["mycollection"]
    data = request.json
    collection.update_one({'_id': ObjectId(id)}, {'$set': data})
    return jsonify({'status': 'success'})

@app.route('/collection/<id>', methods=['DELETE'])
def delete_document(id):
    collection = db["mycollection"]
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)

