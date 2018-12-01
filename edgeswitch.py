# edgeswitch.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect,time

# Variables
linux_pc = "192.168.1.199"
switch = "192.168.1.2"
firmware = "ES-eswh.v1.7.4.5075842.stk"
tftp = "copy tftp://" + linux_pc + "/" + firmware + " backup"
creds = "ubnt"
new_user = "ChangeMe123"
new_pass = "ChangeMe123"
priv = " level 15"
unms_key = "YourKeyHere"
tn = pexpect.spawn("telnet " + switch)

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

def default_login():
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(">")
    tn.sendline("enable")
    tn.expect(":")
    tn.sendline(creds)
    tn.expect("#")

def add_new_user():
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

def firmware_check():
    tn.sendline("show bootvar")
    tn.expect("Current")

def update_firmware():
    tn.sendline(switch_tftp)
    tn.expect("(y/n)")
    tn.sendline("y")
    time.sleep(300)
    tn.expect("lly.")

def set_active_reboot():
    tn.sendline("boot system backup")
    tn.expect("#")
    tn.sendline("reload")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.close()

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
    ssh = pexpect.spawn("ssh " + new_user + "@" + switch)
    ssh.expect("password:")
    ssh.sendline(new_pass)
    ssh.expect(">")
    ssh.sendline("enable")
    ssh.expect("Password:")
    ssh.sendline(new_pass)
    ssh.expect("#")
    ssh.sendline("show version")
    ssh.expect("Serial")
    if "ES-8" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.expect("#")
        ssh.sendline("vlan name 10 PYTHON_VLAN")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no username ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-16-XG" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-16" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-24" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-48" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-5XP" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-10" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "ES-12" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    elif "EP-S16" in ssh.before:
        ssh.sendline("vlan database")
        ssh.expect("#")
        ssh.sendline("vlan 10")
        ssh.sendline("configure")
        ssh.expect("#")
        ssh.sendline("no user ubnt")
        ssh.expect("#")
        #ssh.sendline("service unms key" + unms_key)
        #ssh.expect("#")
        #ssh.sendline("service unms")
        #ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect("#")
        ssh.sendline("write memory")
        ssh.expect("(y/n)")
        ssh.sendline("y")
        ssh.expect("#")
        ssh.sendline("exit")
        ssh.expect(">")
        ssh.sendline("exit")
    else:
        return 26
