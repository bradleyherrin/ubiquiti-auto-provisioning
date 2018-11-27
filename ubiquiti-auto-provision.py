#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import os, sys,telnetlib


# Universal variables
pinging = True
ping = "ping -c 1 "
creds = "ubnt"

# Router variables
router = "192.168.1.1"


# Switch variables
switch = "192.168.1.2"
switch_tftp = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup\n"

# Universal functions
def welcome_message():
        print("-------------------------------------\n".center(40))
        print("Welcome to the Ubiquiti EdgeMax\n".center(40))
        print("Auto-Provisioning Application\n".center(40))
        print("by Bradley Herrin\n".center(40))
        print("-------------------------------------\n".center(40))

# Router functions
def provision_router():
    print('Under Construction')

# Switch functions
def switch_login():
    tn.read_until("User: ")
    tn.write(creds + "\n")
    tn.read_until("Password: ")
    tn.write(creds + "\n")

def switch_firmware_check():
    tn.write("enable\n")
    tn.write(creds + "\n")
    tn.write("show bootvar\n")

def switch_config():
    print('Under Construction')

def update_switch_firmware():
    tn.write(switch_tftp)
    tn.read_until("(y/n)")
    tn.write("y\n")
    tn.read_until("File transfer operation completed sucessfully")

def switch_set_active_reboot():
    tn.write("boot system backup\n")
    tn.write("reload\n")

def provision_switch():
    switch_login()
    switch_firmware_check()
    if "*1.7.4.5075842":
        switch_config()
    else:
        update_switch_firmware()
        switch_set_active_reboot()

# The actual Application
welcome_message()

# Ping check
while pinging:
    if os.system(ping + router) == 0:
        # Provision router
        provision_router()
        break
    elif os.system(ping + switch) == 0:
        tn = telnetlib.Telnet(switch)
        # Provision switch
        provision_switch()
        break
    else:
        # No devices found
        print('No devices found.')
        break
