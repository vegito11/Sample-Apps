from flask import request, jsonify
import uuid

# In-memory storage for players
players_memory = {}

def get_all_players_memory():
    return jsonify(list(players_memory.values())), 200

def get_player_memory(player_id):
    player = players_memory.get(player_id)
    if player:
        return jsonify(player), 200
    return jsonify({'error': 'Player not found'}), 404

def create_player_memory():
    data = request.json
    player_id = str(uuid.uuid4())
    players_memory[player_id] = {
        'id': player_id,
        'name': data.get('name'),
        'matches': data.get('matches'),
        'goals': data.get('goals'),
        'assists': data.get('assists'),
        'club': data.get('club'),
        'age': data.get('age'),
        'country': data.get('country')
    }
    return jsonify(players_memory[player_id]), 201

def update_player_memory(player_id):
    data = request.json
    player = players_memory.get(player_id)
    if player:
        player.update(data)
        return jsonify(player), 200
    return jsonify({'error': 'Player not found'}), 404

def delete_player_memory(player_id):
    if player_id in players_memory:
        del players_memory[player_id]
        return jsonify({'message': 'Player deleted'}), 200
    return jsonify({'error': 'Player not found'}), 404
