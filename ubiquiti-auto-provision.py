#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import os,sys,telnetlib3


# Universal variables
pinging = True
ping = "ping -c 5 "
creds = "ubnt"
linux_pc = "192.168.1.199"

# Router variables
router = "192.168.1.1"
router_tftp = "add system image tftp://192.168.1.199/firmware.tar "

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
def router_login():
    print("Under Construction")

def router_firmware_check():
    ssh.write("show system image\n")

def router_config():
    print("Under Construction")

def update_router_firmware():
    ssh.write(router_tftp)

def router_set_active():
    ssh.write("set system image default-boot\n")

def router_reboot():
    ssh.write("reboot\n")

def provision_router():
    router_login()
    router_firmware_check()
    if "v1.10.7.5127989.181001.1227    (running image) (default boot)":
        router_config()
    elif "v1.10.7.5127989.181001.1227    (default boot)":
        router_reboot()
    elif "v1.10.7.5127989.181001.1227                                  ":
        router_set_active()
        router_reboot()
    else:
        update_router_firmware()
        router_reboot()

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
    if "active  *1.7.4.5075842":
        switch_config()
    elif "backup  *1.7.4.5075842":
        switch_set_active_reboot()
    else:
        update_switch_firmware()
        switch_set_active_reboot()

# The actual application
welcome_message()

# Ping check
while pinging:
    if os.system(ping + router) == 5:
        # Provision router
        provision_router()
    elif os.system(ping + switch) == 5:
        tn = telnetlib.Telnet(switch)
        # Provision switch
        provision_switch()
    else:
        # No devices found
        print('No devices found.')
        break
