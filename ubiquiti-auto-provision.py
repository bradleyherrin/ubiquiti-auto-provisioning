#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect
import subprocess
import edgeswitch
import edgerouter

# Variables
ping = "ping -c 5 "
ping_match = " | grep -c 'bytes from' | grep 5 >/dev/null"
linux_pc = "192.168.1.254"
# Set the below variable only if you want to override the switch firmware version learned in the firmware_path
hardcoded_switch_version = ""
firmware_path = "./tftp/firmware"
config_path = "./tftp/config"
switch = "192.168.1.2"
airmax = "192.168.1.20"
router = "192.168.1.1"
creds = "ubnt"

# Welcome message
print("---------------------------------------------".center(45))
print("Welcome to the Ubiquiti EdgeMax and AirMax".center(45))
print("Auto-Provisioning Application".center(45))
print("by Bradley Herrin and Josh Moore".center(45))
print("---------------------------------------------".center(45))

# Edgeswitch ping check
if subprocess.call(ping + switch + ping_match, shell = True) == 0:
    # Check default access type
    a_type = pexpect.run("telnet " + switch)
    if "Connection refused" in a_type:
        telnet_connection = False
        login_type = "SSH"
    else:
        telnet_connection = True
        login_type = "telnet"
    # Login to switch
    edgeswitch.found_login_um(login_type)
    edgeswitch.default_login(telnet_connection, creds, switch)
    # Check switch model is supported
    if edgeswitch.switch_model() == 26:
        # Error not supported
        edgeswitch.model_not_found_um()
    else:
        # Grab switch model
        model = edgeswitch.switch_model()
        edgeswitch.switch_model_um(model)
        firmware = edgeswitch.latest_switch_firmware(hardcoded_switch_version, firmware_path, model)
        # Check latest firmware for model
        edgeswitch.latest_switch_firmware_um(firmware)
        edgeswitch.firmware_check()
        # Check if latest firmware already on the switch
        if "active  *" + firmware in edgeswitch.connection.before:
            edgeswitch.no_upgrade_um()
        elif "backup   " + firmware in edgeswitch.connection.before:
            edgeswitch.active_um()
            edgeswitch.set_active()
        else:
            # Firmware not on the switch, upgrade
            edgeswitch.updating_firmware_um()
            edgeswitch.update_firmware(linux_pc, firmware)
            if "success" in edgeswitch.connection.before:
                edgeswitch.active_um()
                edgeswitch.set_active()
            else:
                edgeswitch.upgrade_failed_um()
        # Configure switch based on model
        edgeswitch.configuring_um()
        edgeswitch.config(linux_pc, model)
        edgeswitch.configured_successfully_um()
else:
    # No devices found
    print('No switch devices found.')

# Edgerouter ping check
if subprocess.call(ping + router + ping_match, shell = True) == 0:
    print "Found router"
else:
    # No devices found
    print('No router devices found.')

# Airmax ping check
if subprocess.call(ping + airmax + ping_match, shell = True) == 0:
    print "Found airmax"
else:
    # No devices found
    print('No AirMax devices found.')