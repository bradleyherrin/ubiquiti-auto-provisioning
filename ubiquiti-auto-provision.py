#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect,subprocess,time,edgeswitch

# Variables
pinging = True
ping = "ping -c 5 "
ping_match = " | grep -c 'bytes from' | grep 5"
linux_pc = "192.168.1.199"

# Router variables
router = "192.168.1.1"
router_tftp = "add system image tftp://192.168.1.199/firmware.tar "

# Router functions
def router_login():
    print("Router Login Under Construction")

def router_firmware_check():
    ssh.write("show system image")

def router_config():
    print("Router Config Under Construction")

def update_router_firmware():
    ssh.write(router_tftp)

def router_set_active():
    ssh.write("set system image default-boot")

def router_reboot():
    ssh.write("reboot")

# Welcome message
print("---------------------------------------------".center(45))
print("Welcome to the Ubiquiti EdgeMax and AirMax".center(45))
print("Auto-Provisioning Application".center(45))
print("by Bradley Herrin and Josh Moore".center(45))
print("---------------------------------------------".center(45))

# Ping check
while pinging:
    if subprocess.call(ping + router + ping_match, shell=True) == 0:
        # Check router firmware
        print("Provision Router Under Construction".center(45))
        break
    elif subprocess.call(ping + switch + ping_match, shell=True) == 0:
        # Check switch firmware
        edgeswitch.switch_default_login()
        edgeswitch.switch_firmware_check()
        if "active  *1.7.4.5075842" in edgeswitch.tn.before:
            # User message
            print("---------------------------------------------".center(45))
            print("Configuring Switch".center(45))
            print("---------------------------------------------".center(45))
            # Configure switch
            edgeswtich.switch_config()
            if edgeswitch.switch_config() == 26:
                # User message
                print("---------------------------------------------".center(45))
                print("Switch model not found. Switch was not configured.").center(45)
                print("---------------------------------------------".center(45))
                break
            else:
                # User message
                print("---------------------------------------------".center(45))
                print("Switch Configured Sucessfully!".center(45))
                print("---------------------------------------------".center(45))
                # Break to end program
                break
        elif "backup   1.7.4.5075842" in edgeswitch.tn.before:
            # User message
            print("---------------------------------------------".center(45))
            print("Setting backup as active and rebooting.".center(45))
            print("---------------------------------------------".center(45))
            # Set active and reboot
            edgeswitch.switch_set_active_reboot()
            time.sleep(300)
        else:
            # User message
            print("---------------------------------------------".center(45))
            print("Updating switch firmware...".center(45))
            print("---------------------------------------------".center(45))
            # Update switch firmware()
            edgeswitch.update_switch_firmware()
            if "success" in edgeswitch.tn.before:
                print("File transfer operation completed successfully.\n".center(45))
                # User message
                print("---------------------------------------------".center(45))
                print("Setting backup as active and rebooting.".center(45))
                print("---------------------------------------------".center(45))
                # Set active and reboot
                edgeswitch.switch_set_active_reboot()
                time.sleep(300)
            else:
                print("File transfer failed. Please try again.".center(45))
                break
    else:
        # No devices found
        print('No devices found.')
        break
