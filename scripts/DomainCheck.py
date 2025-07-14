import json
import requests
from urllib.parse import quote


otx_api_key = '124d438ef8bb0430e482bf823c6a1531bf866411918a168277f4a9c4ce34f34d'
domain_to_check = 'kbsbridgeloans.com'
encoded_domain = quote(domain_to_check, safe='')
otx_url = f'https://otx.alienvault.com/api/v1/indicators/domain/{encoded_domain}/general'

headers = {
    'X-OTX-API-KEY': otx_api_key,
    'Accept': 'application/json'
}

response = requests.get(otx_url, headers= headers)

if response.status_code == 200:
    data = response.json()
    print(f"Information for URL: {domain_to_check} 👇")
    print(json.dumps(data, indent=3))
elif response.status_code == 404:
    print(f"URL: {domain_to_check} not found in OTX database or no information available.")
    print(f"Error: {response.status_code} - {response.text}")
else:
    print(f"Error: {response.status_code} - {response.text}")