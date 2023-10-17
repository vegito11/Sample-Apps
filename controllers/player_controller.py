from flask import Blueprint, jsonify, request
from models.players import Player
from data.data import Data

player_controller = Blueprint('player_controller', __name__)


@player_controller.route('/players', methods=['GET'])
def get_all_players():
    players = Data.get_all()
    # Serialize the list of players to dictionaries and return as JSON
    serialized_players = [player.to_dict() for player in players]
    return jsonify(serialized_players)

# GET a single player by ID
@player_controller.route('/players/<int:ply_id>', methods=['GET'])
def get_player(ply_id):
    ply = Data.get_by_id(ply_id)
    if ply:
        return jsonify(ply.to_dict())  # Serialize the player to a dictionary and return as JSON
    else:
        return jsonify(f"Player with this {ply_id} ID does not exist."), 404


@player_controller.route('/players', methods=['POST'])
def create_player():
    data = request.json
    try:
        p = Player(data["name"], data["age"], data["club"], data["goals"], data["matches"])
        
        Data.add(p) 
        return jsonify(p.to_dict()), 201 
    except Exception as e:
        return jsonify("Invalid request body"), 400 


@player_controller.route('/players/<int:ply_id>', methods=['PUT'])
def update_player(ply_id):
    ply = Data.get_by_id(ply_id)
    if ply:
        data = request.json
        
        return jsonify(ply.to_dict())
    else:
        return jsonify(f"Player with this {ply_id} ID does not exist."), 404

# Delete a player by ID
@player_controller.route('/players/<int:ply_id>', methods=['DELETE'])
def delete_player(ply_id):
    ply = Data.delete_by_id(ply_id)
    if ply:
        return '', 204
    else:
        return jsonify(f"Player with this {ply_id} ID does not exist."), 404
