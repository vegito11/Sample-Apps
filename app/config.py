import os
from dotenv import load_dotenv

load_dotenv("secrets.env")

class Config:
    AZURE_STORAGE_ACCOUNT = os.getenv("AZURE_STORAGE_ACCOUNT")
    AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME")
    AZURE_SUBSCRIPTION_ID = os.getenv("AZURE_SUBSCRIPTION_ID")
    AZURE_KEYVAULT_NAME = os.getenv("AZURE_KEYVAULT_NAME")
    AZURE_TENANT_ID = os.getenv("AZURE_TENANT_ID")
    AZURE_CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
    AZURE_CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")