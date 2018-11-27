#!/usr/bin/env python3

# hostname.py
# This project is authored by Bradley Herrin.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# User input questions
city = input('What city will this device be installed in? \n')
company = input('What company will this device be installed at? \n')
location_q1 = 'Will this device go in a specific location for this company? '
location_p1 = '(example: Anodizer building at Elixir) '
location_q2 = 'If so what is the name of this location '
location_p2 = '(Leave blank for no specific location)? '
location = input(location_q1 + location_p1 + location_q2 + location_p2 + '\n')
closet = input('MDF or IDF? \n')
device_num_q1 = 'Is this one of multiple similar devices in the MDF/IDF? '
device_num_q2 = 'If so, what number is this one (Leave blank for no number)? '
device_num = input(device_num_q1 + device_num_q2 + '\n')
router_type_q = 'Is this a router? If so, what model '
router_type_p = '(Leave blank for switch)? '
router_type = input(router_type_q + router_type_p + '\n')
hostname_list = [city,company,location,closet,device_num,router_type]

# hostname_list cleanup
if hostname_list.count('') == 3:
    hostname_list.remove('')
    hostname_list.remove('')
    hostname_list.remove('')
    hostname = '-'.join(hostname_list)

elif hostname_list.count('') == 2:
    hostname_list.remove('')
    hostname_list.remove('')
    hostname = '-'.join(hostname_list)

elif hostname_list.count('') == 1:
    hostname_list.remove('')
    hostname = '-'.join(hostname_list)

else:
    hostname = '-'.join(hostname_list)

# Print hostname
print('\n' + hostname)
