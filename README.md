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

curl http://<load-balancer-ip>:5000/volume-usage
```


## Build and Push Docker images to ACR

1. Run the following command to create an ACR:
   
    ```bash
    RG_NAME="management"
    ACR_REPO_NAME="staginguswest2app"
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

	ACR_REPO_NAME="$ACR_REPO_NAME.azurecr.io/az-sample-app:v2"

	docker tag azure-sample-app  $ACR_REPO_NAME
	```

---------------------------------------------------

**Pod Identity Setup (AKS):**
1. **Install Azure Pod Identity:**
```sh
az aks enable-addons --addons azure-keyvault-secrets-provider --resource-group <your-rg> --name <your-aks-cluster>
```

2. **Assign Managed Identity:**

```sh
az identity create --name aks-pod-identity --resource-group <your-rg>
az aks pod-identity add --resource-group <your-rg> --cluster-name <your-aks-cluster> --namespace default --name pod-identity --identity-resource-id <identity-id>
```

3. **Grant Storage Access:**
```sh
az role assignment create --role "Storage Blob Data Reader" --assignee <client-id> --scope /subscriptions/<sub-id>/resourceGroups/<your-rg>/providers/Microsoft.Storage/storageAccounts/<storage-account>
```