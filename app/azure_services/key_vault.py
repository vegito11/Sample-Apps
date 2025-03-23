from azure.keyvault.secrets import SecretClient
from app.azure_services.auth import get_azure_credential
from app.config import Config

def get_secret(secret_name):
    """Retrieves a secret from Azure Key Vault."""
    credential = get_azure_credential()
    keyvault_uri = f"https://{Config.AZURE_KEYVAULT_NAME}.vault.azure.net"
    secret_client = SecretClient(vault_url=keyvault_uri, credential=credential)
    secret = secret_client.get_secret(secret_name)
    return {"name": secret.name, "value": secret.value}

def set_secret(secret_name, secret_value):
    """Sets a secret in Azure Key Vault."""
    credential = get_azure_credential()
    keyvault_uri = f"https://{Config.AZURE_KEYVAULT_NAME}.vault.azure.net"
    secret_client = SecretClient(vault_url=keyvault_uri, credential=credential)
    secret = secret_client.set_secret(secret_name, secret_value)
    return {"name": secret.name, "value": secret.value}