"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Just a small client to make the necessary API endpoint testing.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import requests

endpoint = "http://localhost:8000"

get_response = requests.get(endpoint, json={"query": "Hello world!"})

print(get_response.status_code)
