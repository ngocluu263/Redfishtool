import requests
import json
url = 'https://172.16.4.53/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset'
payload = {'ResetType': 'ForceOff'}
headers = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False, auth=('root', 'calvin'))