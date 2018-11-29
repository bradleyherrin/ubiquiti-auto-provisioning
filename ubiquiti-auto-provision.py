#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect,subprocess,time,atc_switch_config


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
switch_tftp = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup"
tn = pexpect.spawn("telnet " + switch)

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

# Switch functions
def switch_default_login():
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(">")

def switch_firmware_check():
    tn.sendline("enable")
    tn.expect(":")
    tn.sendline(creds)
    tn.expect("#")
    tn.sendline("show bootvar")
    tn.expect("Current")

def update_switch_firmware():
    tn.sendline(switch_tftp)
    tn.expect("(y/n)")
    tn.sendline("y")
    time.sleep(240)
    tn.expect("lly.")

def switch_set_active_reboot():
    tn.sendline("boot system backup")
    tn.expect("#")
    tn.sendline("reload")
    tn.expect("(y/n)")
    tn.sendline("y")

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
        switch_default_login()
        switch_firmware_check()
        if "active  *1.7.4.5075842" in tn.before:
            # User message
            printprint("---------------------------------------------".center(45))
            print("Configuring Switch".center(45))
            printprint("---------------------------------------------".center(45))
            # Configure switch
            atc_switch_config.switch_config()
            if switch_config.switch_config() == 26:
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
        elif "backup   1.7.4.5075842" in tn.before:
            # User message
            print("---------------------------------------------".center(45))
            print("Setting backup as active and rebooting.".center(45))
            print("---------------------------------------------".center(45))
            # Set active and reboot
            switch_set_active_reboot()
            time.sleep(300)
        else:
            # User message
            print("---------------------------------------------".center(45))
            print("Updating switch firmware...".center(45))
            print("---------------------------------------------".center(45))
            # Update switch firmware()
            update_switch_firmware()
            if "successfully" in tn.before:
                print("File transfer operation completed successfully.\n".center(45))
                # User message
                print("---------------------------------------------".center(45))
                print("Setting backup as active and rebooting.".center(45))
                print("---------------------------------------------".center(45))
                # Set active and reboot
                switch_set_active_reboot()
                time.sleep(300)
            else:
                print("File transfer failed. Please try again.".center(45))
                break
    else:
        # No devices found
        print('No devices found.')
        break
