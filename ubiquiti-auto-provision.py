#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Lib import
import os
import sys
import telnetlib

# Variables and functions
pinging = True
router = "192.168.1.1"
switch = "192.168.1.2"
router_ping = os.system("ping -c 1 " + router)
switch_ping = os.system("ping -c 1 " + switch)
creds = "ubnt"
switch_tftp = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup\n"

def provision_router():
    print('Under Construction')

def provision_switch():
    tn = telnetlib.Telnet(switch)

    # Log into the switch
    tn.read_until("User: ")
    tn.write(creds + "\n")
    tn.read_until("Password: ")
    tn.write(creds + "\n")

    # Firmware check
    tn.write("enable\n")
    tn.write(creds + "\n")
    tn.write("show bootvar\n")
    if "*1.7.4.5075842":

        # Write config
        tn.write("baseconfig")
    else:

        # Update firmware
        tn.write(switch_tftp)
        tn.read_until("(y/n)")
        tn.write("y\n")
        tn.read_until("File transfer operation completed sucessfully")

        # Set new firmware as next active and reboot
        tn.write("boot system backup\n")
        tn.write("reload\n")

# Provisioning script
while pinging:
    if router_ping == 0:
        provision_router()
    else switch_ping == 0:
        provision_switch()
