#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin & covered under the GPL-3.0 license.
# The goal of this project is to use Python to auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub - https://github.com/bradleyherrin/ubiquiti-auto-provisioning

import os
import sys
import telnetlib

PINGING = True
ROUTER = "192.168.1.1"
SWITCH = "192.168.1.2"
ROUTERPING = os.system("ping -c 1 " + ROUTER)
SWITCHPING = os.system("ping -c 1 " + SWITCH)
CREDS = "ubnt"
SWITCHTFTP = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup\n"

# Ping check
print ("Searching for devices...")
while PINGING:
    if ROUTERPING == 0:
        print("Under Construction")

    elif SWITCHPING == 0:
        print ("Checking firmware...")
        tn = telnetlib.Telnet(SWITCH)

        # Log into the switch
        tn.read_until("User: ")
        tn.write(CREDS + "\n")
        tn.read_until("Password: ")
        tn.write(CREDS + "\n")

        # Firmware check
        tn.write("enable\n")
        tn.write(CREDS + "\n")
        tn.write("show bootvar\n")

        # Write config or update firmware
        if *1.7.4.5075842:
            print ("Writing base configuration...")
            tn.write("baseconfig")

        else:
            # Update firmware
            print ("Upgrading Firmware...")
            tn.write(SWITCHTFTP)
            tn.read_until("(y/n)")
            tn.write("y\n")
            tn.read_until("File transfer operation completed sucessfully")

            # Set new firmware as next active and reboot
            tn.write("boot system backup\n")
            print("Rebooting switch...")
            tn.write("reload\n")
    else:
        print ("Still searching for devices")
