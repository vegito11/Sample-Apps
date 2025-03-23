from app.azure_services.graph_api import get_authenticated_user_id
from app.azure_services.blob_storage import upload_file_to_blob, list_blobs_in_container
from app.azure_services.key_vault import get_secret, set_secret
from app.azure_services.compute import list_virtual_machines
from app.config import Config

def tmp():
    """Function to test code snippets without running the entire app."""
    print("Testing tmp function...")

    user = get_authenticated_user_id()
    if user:
        print(f"User details: {user}")

    
    vms = list_virtual_machines()
    print(f"Virtual Machines: {vms}")

    # # Example: Test listing blobs in a container
    blobs = list_blobs_in_container(Config.AZURE_CONTAINER_NAME)
    print(f"Blobs in container: {blobs}")

    # Example: Test getting a secret from Key Vault
    secret = get_secret("db-url")
    
    print(f"Secret: {secret}")

    secret = set_secret("db-pass", "43324ed324")

def tmp2():

    file_path = "data/sample_File.txt"

    # Read the file and upload it
    with open(file_path, "rb") as file:
        file_name = file_path.split("/")[-1]  # Extract the file name
        file_content = file.read()
        upload_file_to_blob(file_name, file_content, Config.AZURE_CONTAINER_NAME)
        print(f"File uploaded successfully: {file_name}")

if __name__ == '__main__':
    # tmp()
    tmp2()