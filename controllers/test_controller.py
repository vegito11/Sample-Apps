from flask import Blueprint, jsonify, request
import os
import requests
import traceback


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

@test_controller.route('/app2_call/<path:api_endpoint>', methods=['GET'])
@test_controller.route('/app2_call/', methods=['GET'])
def get_data(api_endpoint=""):
    try:
        
        api_host = os.getenv("APP2_URL", "http://localhost:8080/")
        api_url = f'{api_host}{api_endpoint}'
        
        print(api_url)
        query_params = request.args

        response = requests.get(api_url, params=query_params)
        
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "Failed to retrieve data from the external API"}), 500
    
    except Exception as e:
        # traceback.print_exc()
        return jsonify({"error": str(e)}), 500    