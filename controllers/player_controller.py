from flask import Blueprint, jsonify, request

# Import Player model and Data (assuming they are correctly defined)
from models.players import Player
from data.data import Data

# Create a Blueprint
player_controller = Blueprint('player_controller', __name__)

# GET all players
@player_controller.route('/players', methods=['GET'])
def get_all_players():
    players = Data.get_all()  # Assuming you have a method to fetch all players
    # Serialize the list of players to dictionaries and return as JSON
    serialized_players = [player.to_dict() for player in players]
    return jsonify(serialized_players)

# GET a single player by ID
@player_controller.route('/players/<int:ply_id>', methods=['GET'])
def get_player(ply_id):
    ply = Data.get_by_id(ply_id)  # Assuming you have a method to get a player by ID
    if ply:
        return jsonify(ply.to_dict())  # Serialize the player to a dictionary and return as JSON
    else:
        return jsonify(f"Player with this {ply_id} ID does not exist."), 404

# Create a new player
@player_controller.route('/players', methods=['POST'])
def create_player():
    data = request.json
    try:
        p = Player(data["name"], data["age"], data["club"], data["goals"], data["matches"])
        # Assuming Player constructor is correctly defined
        Data.add(p)  # Assuming you have a method to add a player
        return jsonify(p.to_dict()), 201  # Serialize the player to a dictionary and return as JSON
    except Exception as e:
        return jsonify("Invalid request body"), 400  # Correct the status code

# Update a player by ID (PUT)
@player_controller.route('/players/<int:ply_id>', methods=['PUT'])
def update_player(ply_id):
    ply = Data.get_by_id(ply_id)
    if ply:
        data = request.json
        # Update 'ply' with 'data' as needed
        return jsonify(ply.to_dict())  # Serialize the player to a dictionary and return as JSON
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
