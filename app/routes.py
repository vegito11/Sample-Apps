from flask import jsonify, request
from app.azure_services.blob_storage import upload_file_to_blob, list_blobs_in_container
from app.azure_services.key_vault import get_secret, set_secret
from app.azure_services.compute import list_virtual_machines
from app.config import Config

def init_routes(app):   
    @app.route('/')
    def home():
        return "Azure Management App"

    @app.route('/list-vms')
    def list_vms():
        try:
            vms = list_virtual_machines()
            return jsonify(vms)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/get-secret/<secret_name>')
    def get_secret_route(secret_name):
        try:
            secret = get_secret(secret_name)
            return jsonify(secret)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/create-secret', methods=['POST'])
    def create_secret_route():
        try:
            data = request.json
            secret = set_secret(data['name'], data['value'])
            return jsonify(secret)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    @app.route('/upload-file', methods=['POST'])
    def upload_file():
        """
        Uploads a file to Azure Blob Storage.
        """
        try:
            if 'file' not in request.files:
                return jsonify({"error": "No file provided"}), 400

            file = request.files['file']
            if file.filename == '':
                return jsonify({"error": "No file selected"}), 400

            # Read the file content
            file_content = file.read()
            file_name = file.filename

            # Upload the file to Azure Blob Storage
            filename = upload_file_to_blob(file_name, file_content, Config.AZURE_CONTAINER_NAME)
            return jsonify({"message": "File uploaded successfully", "filename": filename})
        except Exception as e:
            return jsonify({"error": str(e)}), 500       

    @app.route('/list-files')
    def list_files_route():
        try:
            files = list_blobs_in_container(Config.AZURE_CONTAINER_NAME)
            return jsonify({"files": files})
        except Exception as e:
            return jsonify({"error": str(e)}), 500