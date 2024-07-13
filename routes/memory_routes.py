from flask import Blueprint, jsonify
from controllers.memory_controller import (
    get_all_players_memory,
    get_player_memory,
    create_player_memory,
    update_player_memory,
    delete_player_memory
)

memory_bp = Blueprint('memory', __name__)

@memory_bp.route('/healthcheck', methods=['GET'])
def health_check():
    return jsonify({'status': 'up', 'message': 'Application is running.'}), 200

@memory_bp.route('/players', methods=['GET'])
def get_players_memory():
    return get_all_players_memory()

@memory_bp.route('/player/<player_id>', methods=['GET'])
def get_single_player_memory(player_id):
    return get_player_memory(player_id)

@memory_bp.route('/player', methods=['POST'])
def post_player_memory():
    return create_player_memory()

@memory_bp.route('/player/<player_id>', methods=['PUT'])
def put_player_memory(player_id):
    return update_player_memory(player_id)

@memory_bp.route('/player/<player_id>', methods=['DELETE'])
def delete_single_player_memory(player_id):
    return delete_player_memory(player_id)
