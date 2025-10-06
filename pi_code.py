import requests
import json
import sys

# API endpoint
url = "http://192.168.110.19:5000"



# Data to be sent (in JSON format)
payload = {
    "message": " "
}
if len(sys.argv) > 1:
    payload['message'] = str(sys.argv[1])
    print(f"New message: {sys.argv[1]}")

# Request headers
headers = {
    "Content-Type": "application/json",
}

try:
    # Send the POST request
    response = requests.post(url + "/data", headers=headers, data=json.dumps(payload))

    # Check for successful response
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

    # Process the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.json())

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")