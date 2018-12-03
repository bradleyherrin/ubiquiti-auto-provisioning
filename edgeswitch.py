# edgeswitch.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect
import time

# Variables
linux_pc = "192.168.1.199"
switch = "192.168.1.2"
firmware = "ES-eswh.v1.7.4.5075842.stk"
ESXGfirmware = "ES-esgh.v1.8.0.5106045.stk"
ESXfirmware = "ESX.1.1.0.bix"
ESXPfirmware = "SW.v1.4.1.32323.180315.1259.bin"
tftp = "copy tftp://" + linux_pc + "/" + firmware + " backup"
creds = "ubnt"
new_user = "ChangeMe123"
new_pass = "ChangeMe123"
priv = " level 15"
unms_key = "YourKeyHere"
tn = pexpect.spawn("telnet " + switch)
ssh1 = pexpect.spawn("ssh " + creds + "@" + switch)

# Functions


def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring Switch".center(45))
    print("---------------------------------------------".center(45))


def new_user_um():
    print("---------------------------------------------".center(45))
    print("Adding new user to switch".center(45))
    print("---------------------------------------------".center(45))


def model_not_found_um():
    print("---------------------------------------------".center(45))
    print("Switch model not found. Switch was not configured.").center(45)
    print("---------------------------------------------".center(45))


def configured_successfully_um():
    print("---------------------------------------------".center(45))
    print("Switch Configured Successfully!".center(45))
    print("---------------------------------------------".center(45))


def active_reboot_um():
    print("---------------------------------------------".center(45))
    print("Setting backup as active and rebooting.".center(45))
    print("---------------------------------------------".center(45))


def updating_firmware_um():
    print("---------------------------------------------".center(45))
    print("Updating switch firmware...".center(45))
    print("---------------------------------------------".center(45))


def tn_default_login():
    tn.expect("User:")
    tn.sendline(creds)
    tn.expect("Password:")
    tn.sendline(creds)
    tn.expect(">")
    tn.sendline("enable")
    tn.expect("Password:")
    tn.sendline(creds)
    tn.expect("#")


def tn_add_new_user():
    tn.sendline("configure")
    tn.expect("#")
    tn.sendline("username " + new_user + " password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")

def tn_firmware_check():
    tn.sendline("show bootvar")
    tn.expect("Current")


def tn_update_firmware():
    tn.sendline(tftp)
    tn.expect("(y/n)")
    tn.sendline("y")
    time.sleep(240)
    tn.expect("lly.")


def tn_set_active_reboot():
    tn.sendline("boot system backup")
    tn.expect("#")
    tn.sendline("reload")
    tn.expect("(y/n)")
    tn.sendline("y")


def ssh_default_login():
    ssh1.expect("password:")
    ssh1.sendline(creds)
    ssh1.expect(">")
    ssh1.sendline("enable")
    ssh1.expect("Password:")
    ssh1.sendline(creds)
    ssh1.expect("#")


def ssh_add_new_user():
    ssh1.sendline("configure")
    ssh1.expect("#")
    ssh1.sendline("username " + new_user + " password " + new_pass + priv)
    ssh1.expect("#")
    ssh1.sendline("exit")
    ssh1.expect("#")
    ssh1.sendline("write memory")
    ssh1.expect("(y/n)")
    ssh1.sendline("y")
    ssh1.expect("#")


def ssh_firmware_check():
    ssh1.sendline("show bootvar")
    ssh1.expect("Current")


def ssh_update_firmware():
    ssh1.sendline(tftp)
    ssh1.expect("(y/n)")
    ssh1.sendline("y")
    time.sleep(240)
    ssh1.expect("lly.")


def ssh_set_active_reboot():
    ssh1.sendline("boot system backup")
    ssh1.expect("#")
    ssh1.sendline("reload")
    ssh1.expect("(y/n)")
    ssh1.sendline("y")

# Use this section to build your own configs
# using tn.sendline and tn.expect. Currently
# all this does is add a new vlan, remove
# the default user "ubnt", and enable UNMS.
# Make sure to add your key to the unms_key
# variable and uncomment the lines in the
# switch config. The idea for this file is
# is that you would build out configs for
# each model you need to provision. Scroll
# down to see the logic used to check for the
# switch model.


def config():
    ssh2 = pexpect.spawn("ssh " + new_user + "@" + switch)
    ssh2.expect("password:")
    ssh2.sendline(new_pass)
    ssh2.expect(">")
    ssh2.sendline("enable")
    ssh2.expect("Password:")
    ssh2.sendline(new_pass)
    ssh2.expect("#")
    ssh2.sendline("show version")
    ssh2.expect("Serial")
    if "ES-8" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.expect("#")
        ssh2.sendline("vlan name 10 PYTHON_VLAN")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no username ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    elif "ES-16" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no user ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    elif "ES-24" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no user ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    elif "ES-48" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no user ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    elif "ES-12" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no user ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    elif "EP-S16" in ssh2.before:
        ssh2.sendline("vlan database")
        ssh2.expect("#")
        ssh2.sendline("vlan 10")
        ssh2.sendline("configure")
        ssh2.expect("#")
        ssh2.sendline("no user ubnt")
        ssh2.expect("#")
        # ssh2.sendline("service unms key" + unms_key)
        # ssh2.expect("#")
        # ssh2.sendline("service unms")
        # ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect("#")
        ssh2.sendline("write memory")
        ssh2.expect("(y/n)")
        ssh2.sendline("y")
        ssh2.expect("#")
        ssh2.sendline("exit")
        ssh2.expect(">")
        ssh2.sendline("exit")
    else:
        return 26
