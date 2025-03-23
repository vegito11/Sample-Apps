from azure.mgmt.compute import ComputeManagementClient
from app.azure_services.auth import get_azure_credential
from app.config import Config

def list_virtual_machines():
    """Lists all virtual machines in the subscription."""
    credential = get_azure_credential()
    compute_client = ComputeManagementClient(credential, Config.AZURE_SUBSCRIPTION_ID)
    vms = compute_client.virtual_machines.list_all()
    return [vm.as_dict() for vm in vms]