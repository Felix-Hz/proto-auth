"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Just a small client to make the necessary API endpoint testing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import requests

PORT = 8000
DOMAIN = "127.0.0.1"
API = "auth_api"

ENDPOINT = f"http://{DOMAIN}:{PORT}/{API}"

response = requests.get(ENDPOINT, json={"query": "Hello world!"})

print(response.text)
