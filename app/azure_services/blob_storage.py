from azure.storage.blob import BlobServiceClient
from app.azure_services.auth import get_azure_credential
from app.config import Config

def upload_file_to_blob(file_name, file_content, container_name):
    credential = get_azure_credential()
    blob_service_client = BlobServiceClient(
        f"https://{Config.AZURE_STORAGE_ACCOUNT}.blob.core.windows.net",
        credential=credential
    )
    container_client = blob_service_client.get_container_client(container_name)
    container_client.upload_blob(file_name, file_content, overwrite=True)
    return file_name


def list_blobs_in_container(container_name):
    """Lists all blobs in a container."""
    credential = get_azure_credential()
    blob_service_client = BlobServiceClient(
        f"https://{Config.AZURE_STORAGE_ACCOUNT}.blob.core.windows.net",
        credential=credential
    )
    container_client = blob_service_client.get_container_client(container_name)
    return [blob.name for blob in container_client.list_blobs()]