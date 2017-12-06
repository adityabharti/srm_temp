from srm_client.client import SrmClient
import json


with SrmClient('10.137.6.72:9086/vcdr/extapi/sdk', 'administrator@vsphere.local', 'Nutanix/4u').open() as client:

adfa

'''with SrmClient('10.1.56.117:9086/vcdr/extapi/sdk', 'administrator@hqdevsrmsso.local', 'Nutanix/4u').open() as client:
#with SrmClient('10.137.6.72:9086/vcdr/extapi/sdk', 'administrator@vsphere.local', 'Nutanix/4u').open() as client:
  #print client.get_recovery_plans()
  print "\n\nSite name:\n"
  print client.get_site_name()
  print "\n\nRetrieve Content:\n"
  print json.dumps(client.retrieve_content(), indent=3)
  print "\n\nList Paired Site:\n"
  print json.dumps(client.get_paired_site(), indent=5)
  print "\n\nListing Inventory Mappings:\n"
  print client.list_inventory_mappings()
  #print json.dumps(client.list_inventory_mappings(), indent=3, sort_keys=True)
'''