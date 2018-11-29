#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect,subprocess,time,switch_config


# Universal variables
pinging = True
ping = "ping -c 5 "
ping_match = " | grep -c 'bytes from' | grep 5"
creds = "ubnt"
linux_pc = "192.168.1.199"
unms_key = "YOUR KEY HERE"

# Router variables
router = "192.168.1.1"
router_tftp = "add system image tftp://192.168.1.199/firmware.tar "

# Switch variables
switch = "192.168.1.2"
switch_tftp = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup\n"
tn = pexpect.spawn("telnet " + switch)
new_user = "CHANGE ME"
new_pass = "CHANGE ME"
priv = " level 15"

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
def switch_default_login():
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(">")

def switch_new_login():
    tn.expect(":")
    tn.sendline(new_user)
    tn.expect(":")
    tn.sendline(new_pass)
    tn.expect(">")
    tn.sendline("enable")
    tn.expect("#")
    tn.sendline("configure")
    tn.expect("#")

def switch_firmware_check():
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(">")
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
    time.sleep(300)
    tn.expect("#")

def switch_set_active_reboot():
    tn.sendline("boot system backup")
    tn.expect("#")
    tn.sendline("reload")

# Welcome message
print("------------------------------------------".center(40))
print("Welcome to the Ubiquiti EdgeMax and AirMax".center(40))
print("Auto-Provisioning Application".center(40))
print("by Bradley Herrin and Josh Moore".center(40))
print("------------------------------------------".center(40))

# Ping check
while pinging:
    if subprocess.call(ping + router + ping_match, shell=True) == 0:
        # Check router firmware
        print("Provision Router Under Construction")
        break
    elif subprocess.call(ping + switch + ping_match, shell=True) == 0:
        # Check switch firmware
        switch_login()
        switch_firmware_check()
            if "active  *1.7.4.5075842" in tn.before:
                # User message
                print("------------------".center(40))
                print("Configuring Switch".center(40))
                print("------------------".center(40))
                # Configure switch
                switch_config.switch_config()
                if switch_config.switch_config() == 26:
                    # User message
                    print("--------------------------------------------------")
                    print("Switch model not found. Switch was not configured.")
                    print("--------------------------------------------------")
                    break
                else:
                    # User message
                    print("------------------------------".center(40))
                    print("Switch Configured Sucessfully!".center(40))
                    print("------------------------------".center(40))
                    # Break to end program
                    break
            elif "backup  *1.7.4.5075842" in tn.before:
                # User message
                print("---------------------------------------".center(40))
                print("Setting backup as active and rebooting.".center(40))
                print("---------------------------------------".center(40))
                # Set active and reboot
                switch_set_active_reboot()
                # This break is temporary. Eventually it
                # will be replaced with a time.sleep(300)
                break
            else:
                # User message
                print("---------------------------".center(40))
                print("Updating switch firmware...".center(40))
                print("---------------------------\n".center(40))
                # Update switch firmware()
                update_switch_firmware()
                if "sucessfully" in tn.before:
                    print("File transfer operation completed sucessfully.\n")
                else:
                    print("File transfer failed. Please try again.")
                    break
                # User message
                print("---------------------------------------".center(40))
                print("Setting backup as active and rebooting.".center(40))
                print("---------------------------------------".center(40))
                # Set active and reboot
                switch_set_active_reboot()
                # This break is temporary. Eventually it
                # will be replaced with a time.sleep(300)
                break
    else:
        # No devices found
        print('No devices found.')
        break
