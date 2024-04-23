from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def initialize_blob_service_client():
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(
        account_url="https://racky.blob.core.windows.net",
        credential=credential)
    return blob_service_client

def upload_blob(container_name, blob_name, file_path):
    blob_service_client = initialize_blob_service_client()
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"Blob {blob_name} uploaded to container {container_name}")
