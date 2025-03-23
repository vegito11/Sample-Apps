import requests
from app.azure_services.auth import get_azure_credential

def get_authenticated_user_id():
    """Retrieves the authenticated user's details using Microsoft Graph API."""
    credential = get_azure_credential()
    
    # Get a token for Microsoft Graph API
    token = credential.get_token("https://graph.microsoft.com/.default")

    # Microsoft Graph API endpoint for the authenticated user
    GRAPH_API_ENDPOINT = 'https://graph.microsoft.com/v1.0/me'

    headers = {
        'Authorization': f'Bearer {token.token}',  # Use token.token, not the token object
        'Content-Type': 'application/json'
    }

    response = requests.get(GRAPH_API_ENDPOINT, headers=headers)

    if response.status_code == 200:
        user = response.json()
        print(f"Authenticated User Principal Name: {user['userPrincipalName']}")
        print(f"Authenticated User ID: {user['id']}")
        return user
    else:
        print(f"Failed to retrieve user details. Status code: {response.status_code}")
        print(response.json())
        return None