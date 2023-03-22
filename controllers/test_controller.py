from flask import Blueprint, jsonify, request
import os

test_controller = Blueprint('test_controller', __name__)

@test_controller.route('/test', methods=['GET'])
def test():
    PASSWORD = os.getenv("VAULT_PASSWORD", "default@123")
    USERNAME = os.getenv("VAULT_USER", "default_user")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "default_name")
    
    return jsonify({
        "password": PASSWORD,
        "username": USERNAME,
        "env_name": ENVIRONMENT
    })