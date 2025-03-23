from azure.identity import DefaultAzureCredential
from app.config import Config

def get_azure_credential():
    """Returns Azure credentials using DefaultAzureCredential."""
    return DefaultAzureCredential()