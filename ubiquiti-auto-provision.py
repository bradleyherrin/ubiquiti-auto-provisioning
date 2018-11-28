#!/usr/bin/env python3

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin with help from Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import subprocess,sys,telnetlib


# Universal variables
pinging = True
ping = "ping -c 5 "
ping_match = " | grep -c 'bytes from' | grep 5"
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
    print("Router Login Under Construction")

def router_firmware_check():
    ssh.write("show system image\n")

def router_config():
    print("Router Config Under Construction")

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
    tn.read_until(b"User:")
    tn.write(creds.encode("utf-8") + b"\n")
    tn.read_until(b"Password:")
    tn.write(creds.encode("utf-8") + b"\n")

def switch_firmware_check():
    tn.write(b"enable\n")
    tn.write(creds.encode("utf-8") + b"\n")
    tn.write(b"show bootvar\n")
    bootvar = tn.write(b"show bootvar\n")

def switch_config():
    print('Switch Config Under Construction')

def update_switch_firmware():
    tn.write(switch_tftp.encode("utf-8"))
    tn.read_until(b"(y/n)")
    tn.write(b"y\n")
    tn.read_until(b"File transfer operation completed sucessfully")

def switch_set_active_reboot():
    tn.write(b"boot system backup\n")
    tn.write(b"reload\n")

def provision_switch():
    switch_login()
    switch_firmware_check()
    if "active  *1.7.4.5075842" in bootvar:
        switch_config()
    elif "backup  *1.7.4.5075842" in bootvar:
        switch_set_active_reboot()
    else:
        update_switch_firmware()
        switch_set_active_reboot()

# The actual application
welcome_message()

# Ping check
while pinging:
    if subprocess.call(ping + router + ping_match, shell=True) == 0:
        # Provision router
        print("Provision Router Under Construction")
        break
    elif subprocess.call(ping + switch + ping_match, shell=True) == 0:
        tn = telnetlib.Telnet(switch)
        # Provision switch
        provision_switch()
        print("The switch has been configured!")
        break
    else:
        # No devices found
        print('No devices found.')
        break
