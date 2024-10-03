from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask import Flask, request

app = Flask(__name__)

# Replace with your Azure Blob Storage connection string
AZURE_CONNECTION_STRING = "AZURE_CONNECTION_STRING"
CONTAINER_NAME = "logcontainer"

def log_request(request):
    try:
        # Initialize the BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)

        # Log data - similar to what was done in GCP
        log_data = f"{request.remote_addr} - {request.method} - {request.url}\n"

        # Name your blob (log file)
        blob_name = "logs.txt"

        # Get a blob client (this refers to your file in Blob Storage)
        blob_client = container_client.get_blob_client(blob_name)

        # Check if the blob already exists, if it does, download the current log and append to it
        try:
            existing_logs = blob_client.download_blob().readall().decode('utf-8')
            log_data = existing_logs + log_data
        except Exception as e:
            # If the blob does not exist, start fresh
            print(f"Blob not found or another error: {str(e)}")

        # Upload (or update) the log file
        blob_client.upload_blob(log_data, overwrite=True)

        return "Request logged successfully!", 200

    except Exception as e:
        return f"Failed to log request: {str(e)}", 500

@app.route('/log', methods=['GET', 'POST'])
def log():
    return log_request(request)

if __name__ == "__main__":
    app.run(debug=True)
