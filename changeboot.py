import requests
import json

url = 'https://172.16.4.53/redfish/v1/Systems/System.Embedded.1'
payload = {'Boot': {'BootSourceOverrideTarget': 'BiosSetup'} }

headers = {'content-type': 'application/json'}
response = requests.patch(url, data=json.dumps(payload), headers=headers, verify=False, auth=('root', 'calvin'))