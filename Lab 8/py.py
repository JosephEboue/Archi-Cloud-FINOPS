import requests
import json

# Replace with your actual subscription key and endpoint
subscription_key = '8508285aec1d47ad9a6f018fc13e8713' 
endpoint = 'https://joe-cognitive-service.cognitiveservices.azure.com/text/analytics/v3.1/sentiment'

documents = {
    "documents": [
        {"id": "1", "language": "en", "text": "I love learning about Azure! It's fantastic."},
        {"id": "2", "language": "en", "text": "I'm frustrated with slow response times."}
    ]
}

headers = {
    'Ocp-Apim-Subscription-Key': subscription_key,
    'Content-Type': 'application/json'
}

# Call the Text Analytics API
response = requests.post(endpoint, headers=headers, json=documents)

# Check if the request was successful
if response.status_code == 200:
    # Print the response (sentiment analysis results)
    result = response.json()
    print(json.dumps(result, indent=4))
else:
    print(f"Error: {response.status_code} - {response.text}")
