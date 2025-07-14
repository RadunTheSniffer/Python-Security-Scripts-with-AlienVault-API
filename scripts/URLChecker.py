import json
import requests
from urllib.parse import quote


otx_api_key = 'your-otx-api-key'
url_to_check = 'wnt-some-push.net'
encoded_url = quote(url_to_check, safe='')
otx_url = f'https://otx.alienvault.com/api/v1/indicators/url/{encoded_url}/general'

headers = {
    'X-OTX-API-KEY': otx_api_key,
    'Accept': 'application/json'
}

response = requests.get(otx_url, headers= headers)

if response.status_code == 200:
    data = response.json()
    print(f"Information for URL: {url_to_check} 👇")
    print(json.dumps(data, indent=3))
elif response.status_code == 404:
    print(f"URL: {url_to_check} not found in OTX database or no information available.")
    print(f"Error: {response.status_code} - {response.text}")
else:
    print(f"Error: {response.status_code} - {response.text}")
