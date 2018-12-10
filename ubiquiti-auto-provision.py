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
import airmax

# Variables
ping = "ping -c 5 "
ping_match = " | grep -c 'time=' | grep 5 >/dev/null"
linux_pc = "192.168.1.254"
# Set the below variable only if you want to override the switch firmware version learned in the firmware_path
firmware_path = "./tftp/firmware/"
config_path = "./tftp/config/"
switch = "192.168.1.2"
ap = "192.168.1.20"
router = "192.168.1.1"
creds = "ubnt"

# Welcome message
print("---------------------------------------------".center(45))
print("Welcome to the Ubiquiti EdgeMax and AirMax".center(45))
print("Auto-Provisioning Application".center(45))
print("by Bradley Herrin and Josh Moore".center(45))
print("---------------------------------------------".center(45))

# Edgeswitch ping check
if switch and subprocess.call(ping + switch + ping_match, shell = True) == 0:
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
        firmware = edgeswitch.latest_switch_firmware(firmware_path, model)
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
            edgeswitch.update_firmware(linux_pc)
            if "success" in edgeswitch.connection.before:
                edgeswitch.active_um()
                edgeswitch.set_active()
            else:
                edgeswitch.upgrade_failed_um()
        # Configure switch based on model
        edgeswitch.configuring_um()
        edgeswitch.config(linux_pc, model)
        edgeswitch.configured_successfully_um()
elif not switch:
    print "Switch provisioning disabled, continuing to next step..."
else:
    # No devices found
    print('No switch devices found.')

# Edgerouter ping check
if router and subprocess.call(ping + router + ping_match, shell = True) == 0:
    print "Found router"
elif not router:
    print "Router provisioning disabled, continuing to next step..."
else:
    # No devices found
    print('No router devices found.')

# Airmax ping check
if ap and subprocess.call(ping + ap + ping_match, shell = True) == 0:
    # Login to airmax
    airmax.found_login_um()
    airmax.default_login(creds, ap)
    # Check airmax model is supported
    if airmax.airmax_model() == 26:
        # Error not supported
        airmax.model_not_found_um()
    else:
        # Grab airmax model
        model = airmax.airmax_model()
        airmax.airmax_model_um(model)
        firmware = airmax.latest_airmax_firmware(firmware_path, model)
        # Check latest firmware for model
        airmax.latest_airmax_firmware_um(firmware)
        airmax.firmware_check()
        # Check if latest firmware already on the switch
        if firmware in airmax.connection.before:
            airmax.no_upgrade_um()
            # Configure airmax based on model
            airmax.configuring_um()
            airmax.config(ap, model, config_path)
            airmax.configured_successfully_um()
        else:
            # Firmware not on the airmax, upgrade
            airmax.updating_firmware_um()
            airmax.update_firmware(ap, creds, firmware, firmware_path)
            edgeswitch.active_um()
            edgeswitch.set_active()
elif not ap:
    print "Airmax provisioning disabled, continuing to next step..."
else:
    # No devices found
    print('No AirMax devices found.')
print "Script execution complete."