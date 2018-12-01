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
ssh = pexpect.spawn("ssh " + new_user + "@" + switch)

# Functions
def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring Switch".center(45))
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

def new_login():
    ssh.expect("password:")
    ssh.sendline(new_pass)
    ssh.expect(">")
    ssh.sendline("enable")
    ssh.expect("Password:")
    ssh.sendline(new_pass)
    ssh.expect("#")

def add_new_user():
    tn.sendline("configure")
    tn.expect("(Config)#")
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("(Config)#")
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
    time.sleep(240)
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

def switch8():
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

def switch16():
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

def switch24():
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

def switch48():
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

def switch5():
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

def switch10():
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

def switch12():
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

def switchS16():
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

def switch16XG():
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

# Here is the logic that will check for which config to serve.
# Keep in mind that the order is important. For example, the
# ES-16-XG comes before ES-16 switch to prevent the switch16()
# function from being pushed to an ES-16-XG.

def config():
    ssh.sendline("show version")
    ssh.expect("Serial")
    if "ES-8" in ssh.before:
        switch8()
    elif "ES-16-XG" in ssh.before:
        switch16XG()
    elif "ES-16" in ssh.before:
        switch16()
    elif "ES-24" in ssh.before:
        switch24()
    elif "ES-48" in ssh.before:
        switch48()
    elif "ES-5XP" in ssh.before:
        switch5()
    elif "ES-10" in ssh.before:
        switch10()
    elif "ES-12" in ssh.before:
        switch12()
    elif "EP-S16" in ssh.before:
        switchS16()
    else:
        return 26
