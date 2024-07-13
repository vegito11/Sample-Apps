from flask import request, jsonify
from pymongo import MongoClient, errors
from bson.objectid import ObjectId
import os

# Establish connection to MongoDB
mongo_url = os.getenv('MONGO_URL')
mongo_username = os.getenv('MONGO_USERNAME')
mongo_password = os.getenv('MONGO_PASSWORD')

try:
    client = MongoClient(mongo_url, username=mongo_username, password=mongo_password, serverSelectionTimeoutMS=5000)
    db = client.mydatabase
    collection = db.players
except errors.ServerSelectionTimeoutError as err:
    client = None
    db = None
    collection = None
    print(f"Failed to connect to MongoDB: {err}")

def get_all_players():
    if collection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    players = list(collection.find())
    for player in players:
        player['_id'] = str(player['_id'])
    return jsonify(players), 200

def get_player(player_id):
    if collection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    player = collection.find_one({'_id': ObjectId(player_id)})
    if player:
        player['_id'] = str(player['_id'])
        return jsonify(player), 200
    return jsonify({'error': 'Player not found'}), 404

def create_player():
    if collection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    data = request.json
    result = collection.insert_one(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

def update_player(player_id):
    if collection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    data = request.json
    result = collection.update_one({'_id': ObjectId(player_id)}, {'$set': data})
    if result.matched_count:
        return jsonify({'message': 'Player updated'}), 200
    return jsonify({'error': 'Player not found'}), 404

def delete_player(player_id):
    if collection is None:
        return jsonify({'error': 'Database connection failed'}), 500
    result = collection.delete_one({'_id': ObjectId(player_id)})
    if result.deleted_count:
        return jsonify({'message': 'Player deleted'}), 200
    return jsonify({'error': 'Player not found'}), 404
