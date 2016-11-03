import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

system = requests.get('https://172.16.4.53/redfish/v1/Systems/System.Embedded.1',
                      verify=False,auth=('root','calvin'))
storage = requests.get('https://172.16.4.53/redfish/v1/Systems/System.Embedded.1/Storage/Controllers/RAID.Integrated.1-1',
                       verify=False,auth=('root','calvin'))
systemData = system.json()
storageData = storage.json()

print(storageData)
#print(systemData)

print("Model: {}".format(systemData[u'Model']))
print("Manufacturer: {}".format(systemData[u'Manufacturer']))
print("Service tag {}".format(systemData[u'SKU']))
print("Serial number: {}".format(systemData[u'SerialNumber']))
print("Hostname: {}".format(systemData[u'HostName']))
print("Power state: {}".format(systemData[u'PowerState']))
print("Asset tag: {}".format(systemData[u'AssetTag']))
print("Memory size: {}".format(systemData[u'MemorySummary'][u'TotalSystemMemoryGiB']))
print("CPU type: {}".format(systemData[u'ProcessorSummary'][u'Model']))
print("Number of CPUs: {}".format(systemData[u'ProcessorSummary'][u'Count']))
print("System status: {}".format(systemData[u'Status'][u'Health']))
print("RAID health: {}".format(storageData[u'Status'][u'Health']))
print("RAID NAME: {}".format(storageData[u'Name']))
print("RAID Model: {}".format(storageData[u'Devices'][1]))
