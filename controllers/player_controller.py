from flask import Blueprint, jsonify, request
from models.players import Player
from data.data import Data

player_controller = Blueprint('player_controller', __name__)

@player_controller.route('/players', methods=['GET'])
def get_all_books():
    players = Data.players_data
    return jsonify(players)

@player_controller.route('/players/<int:ply_id>', methods=['GET'])
def get_book(ply_id):
    
    ply = Data.get_by_id(ply_id)

    if ply:
        return jsonify(ply)
    else:    
        return jsonify (f" Player with this {ply_id} id does not exists !!! "), 404

@player_controller.route('/players', methods=['POST'])
def create_book():

    data = request.json
    try:
        p = Player(data["name"], data["age"], data["club"], data["goals"], data["matches"])
    except Exception as e:
        return jsonify (f" Invalid request body "), 401
    
    return jsonify(p), 201

@player_controller.route('/players/<int:ply_id>', methods=['PUT'])
def update_book(ply_id):
    
    ply = Data.get_by_id(ply_id)

    if ply:
        data = request.json
        
    else:
        return jsonify (f" Player with this {ply_id} id does not exists !!! "), 404
    
    return jsonify(ply)

@player_controller.route('/players/<int:ply_id>', methods=['DELETE'])
def delete_book(ply_id):

    ply = Data.delete_by_id(ply_id)
    if ply:
        return '', 204
    else:
        return jsonify (f" Player with this {ply_id} id does not exists !!! "), 404
