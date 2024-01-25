"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Just a small client to make the necessary API endpoint testing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import requests


# Basic request to attempt connection.

PORT = 8000
DOMAIN = "127.0.0.1"
API = "auth_api"

ENDPOINT = f"http://{DOMAIN}:{PORT}/{API}"

response = requests.get(ENDPOINT, json={"query": "Hello world!"})

print(f"1. status_code= {response.status_code}")

# Register POST request. 

REGISTER_ENDPOINT = f"http://{DOMAIN}:{PORT}/{API}/register/"

registration_data = {
    "username": "Joe Diaz",
    "email": "joe@diaz.com",
    "password": "joe_diaz_123",
}

registration_response = requests.post(REGISTER_ENDPOINT, json=registration_data)

print(f"2. status_code= {registration_response.status_code}")
# try:
print(registration_response.text)
# except requests.exceptions.JSONDecodeError:
    # print(registration_response.text)
