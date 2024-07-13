from flask import Blueprint, jsonify
from config import Config 
from pymongo import MongoClient
from controllers.player_controller import (
    get_all_players,
    get_player,
    create_player,
    update_player,
    delete_player
)

player_bp = Blueprint('player', __name__)

mongo_url = Config.MONGO_URL
mongo_username = Config.MONGO_USERNAME
mongo_password = Config.MONGO_PASSWORD

@player_bp.route('/mongocheck', methods=['GET'])
def mongo_check():
    try:
        client = MongoClient(mongo_url, username=mongo_username, password=mongo_password)
        db = client.get_database()  # Replace with your database name if different
        db.command('ping')  # Check if we can ping MongoDB
        client.close()
        return jsonify({'status': 'ok', 'message': 'MongoDB connection successful.'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'MongoDB connection failed: {str(e)}'}), 500

@player_bp.route('/players', methods=['GET'])
def get_players():
    return get_all_players()

@player_bp.route('/player/<player_id>', methods=['GET'])
def get_single_player(player_id):
    return get_player(player_id)

@player_bp.route('/player', methods=['POST'])
def post_player():
    return create_player()

@player_bp.route('/player/<player_id>', methods=['PUT'])
def put_player(player_id):
    return update_player(player_id)

@player_bp.route('/player/<player_id>', methods=['DELETE'])
def delete_single_player(player_id):
    return delete_player(player_id)
