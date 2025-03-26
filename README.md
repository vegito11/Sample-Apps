# Azure Python App

```bash
AZURE_SUBSCRIPTION_ID="XXXXX-XXX-XXX-XXX-XXXXX"
AZURE_KEYVAULT_NAME="XXXXXXXXXXXXX"
AZURE_STORAGE_ACCOUNT="XXXXXX"
AZURE_CONTAINER_NAME="app-data"
```

## Test the App

```sh
export PYTHONPATH=$(pwd)
python -m app.tmp
python app.py

curl -X GET http://localhost:5000/list-vms
```


## Build and Push Docker images to ACR

1. Run the following command to create an ACR:
   
    ```bash
    RG_NAME="management"
    ACR_REPO_NAME="vegitoapp"
    az acr create --resource-group $RG_NAME --name $ACR_REPO_NAME --sku Basic
    ```

2. Once the registry is created, you can verify it by listing all ACRs in your subscription:

 	```bash
 	az acr list --resource-group $RG_NAME --output table
 	```

3. Log in to your ACR using the following command:

 	```bash
 	az acr login --name $ACR_REPO_NAME
 	# Or use below command to get the token printed on CLI
 	az acr login --name $ACR_REPO_NAME --expose-token
 	```

4. Once your ACR is created, you can push and pull Docker images using the following commands:


	```bash
	docker build -t azure-sample-app .

	ACR_REPO_URL="$ACR_REPO_NAME.azurecr.io/az-sample-app:v2"

	docker tag azure-sample-app  $ACR_REPO_URL
	```

---------------------------------------------------

## API Endpoints & Usage

### 1️⃣  List Azure Virtual Machines

  ```sh
  curl -X GET http://localhost:5000/list-vms
  ```

### 2️⃣  Get Secret from Azure Key Vault

  ```sh
  curl -X GET http://localhost:5000/get-secret/db-url
  ```

### 3️⃣  Create a Secret in Azure Key Vault

  ```sh
  curl -X POST http://localhost:5000/create-secret \
       -H "Content-Type: application/json" \
       -d '{"name": "dbpass", "value": "sdfer3243"}'
  ```

### 4️⃣  Upload File to Azure Blob Storage

  ```sh
  curl -X POST http://localhost:5000/upload-file \
       -F "file=@/path/to/your/file.txt"
  ```

### 5️⃣ List Files in Azure Blob Storage

  ```sh
  curl -X GET http://localhost:5000/list-files
  ```



---------------------------------------------------

- [Add workload identity in AKS cluster](https://learn.microsoft.com/en-us/azure/aks/workload-identity-deploy-cluster)

