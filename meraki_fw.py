import meraki
import pprint
import csv

# Defining your API key as a variable in source code is not recommended
API_KEY = 'INSERT_MERAKI_API_KEY_HERE'
# Instead, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/

network_id = 'INSERT_NETWORK_ID_HERE'
organization_id = 'INSERT_ORG_ID_HERE'

dashboard = meraki.DashboardAPI(API_KEY)

l3_response = dashboard.appliance.getNetworkApplianceFirewallL3FirewallRules(
    network_id
)

vpn_response = dashboard.appliance.getOrganizationApplianceVpnVpnFirewallRules(
    organization_id
)

l3_rules = l3_response['rules']
vpn_rules = vpn_response['rules']

headers = ['comment', 'policy', 'protocol', 'srcPort', 'srcCidr', 'destPort', 'destCidr', 'syslogEnabled']

def write_to_csv(**kwargs):
    for file, data in kwargs.items():

        with open(f'{file}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(headers)

            for rule in data:
                writer.writerow(
                    [
                        rule['comment'],
                        rule['policy'],
                        rule['protocol'],
                        rule['srcPort'],
                        rule['srcCidr'],
                        rule['destPort'],
                        rule['destCidr'],
                        rule['syslogEnabled']
                    ]
                )

if __name__ == '__main__':
    write_to_csv(l3=l3_rules, vpn=vpn_rules)