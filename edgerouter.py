# edgerouter.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect

# Variables
router = "192.168.1.1"
linux_pc = "192.168.1.199"
tftp = "add system image tftp://" + linux_pc + "/"
e50firmware = "ER-e50.v1.10.8.5142457.tar"
e100firmware = "ER-e100.v1.10.8.5142440.tar"
e200firmware = "ER-e200.v1.10.8.5142441.tar"
e300firmware = "ER-e300.v1.10.8.5142457.tar"
e1000firmware = "ER-e1000.v1.10.8.5142441.tar"
creds = "ubnt"
new_user = "ChangeMe123"
new_pass = "ChangeMe123"
unms_key = "YourKeyHere"
def_ssh = pexpect.spawn("ssh " + creds + "@" + router)
under_construction = "Router Configuration Under Construction"

# Functions
def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring Router".center(45))
    print("---------------------------------------------".center(45))

def model_not_found_um():
    print("---------------------------------------------".center(45))
    print("Router model not found.".center(45))
    print("Router was not updated or configured.".center(45))
    print("---------------------------------------------".center(45))

def configured_successfully_um():
    print("---------------------------------------------".center(45))
    print("Router Configured Successfully!".center(45))
    print("---------------------------------------------".center(45))

def active_reboot_um():
    print("---------------------------------------------".center(45))
    print("Setting firmware as active and rebooting.".center(45))
    print("---------------------------------------------".center(45))

def updating_firmware_um():
    print("---------------------------------------------".center(45))
    print("Updating router firmware...".center(45))
    print("---------------------------------------------".center(45))

def default_login():
    def_ssh.expect(":")
    def_ssh.sendline(creds)
    def_ssh.expect("$")

def new_login():
    new_ssh.expect(":")
    new_ssh.sendline(new_pass)
    new_ssh.expect("$")
    new_ssh.sendline("configure")
    new_ssh.expect("#")

def firmware_check():
    def_ssh.sendline("show system image")
    def_ssh.expect("(running image) (default boot)")

def version_check():
    def_ssh.sendline("show version")
    def_ssh.expect("HW S/N")

def e50_fw_update():
    def_ssh.sendline(tftp + e50firmware)
    def_ssh.expect("")

def e100_fw_update():
    def_ssh.sendline(tftp + e100firmware)
    def_ssh.expect("")

def e200_fw_update():
    def_ssh.sendline(tftp + e200firmware)
    def_ssh.expect("")

def e300_fw_update():
    def_ssh.sendline(tftp + e300firmware)
    def_ssh.expect("")

def e1000_fw_update():
    def_ssh.sendline(tftp + e1000firmware)
    def_ssh.expect("")

def set_active_reboot():
    def_ssh.sendline("set system image default-boot")
    def_ssh.expect("$")
    def_ssh.sendline("reboot")
    def_ssh.expect("[confirm]")
    def_ssh.sendline("y")

# Use this section to build your own
# configs. Currently all these provide
# the same level of configuration as
# the basic setup wizard when DHCP is
# selected as the WAN connection type.
# Scroll down to see the logic used to
# check for the router model.

def er_x_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_x_sfp_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_10x_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def ep_r6_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def erlite_3_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def erpoe_5_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_8_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_pro8_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def ep_r8_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_4_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_6p_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_12_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

def er_infinity_config():
    #new_ssh = pexpect.spawn("ssh " + new_user + "@" + router)
    print(under_construction)

# Here is the logic that will check for which config to serve.
# Keep in mind that the order is important. For example, the
# EdgeRouter (ER-8) is last, otherwise it will cause the wrong
# function to be pushed. Also, a disclaimer, I don't have an
# ER-8 to test with. I'm assuming it reports "EdgeRouter" as
# the HW Model. If you provison the ER-8 often, I would do a
# show version command on one to be sure.

def config():
    version_check()
    if "EdgeRouter X" in def_ssh.before:
        er_x_config()
    elif "EdgeRouter X SFP" in def_ssh.before:
        er_x_sfp_config()
    elif "EdgeRouter 10X" in def_ssh.before:
        er_10x_config()
    elif "EdgePoint Router 6" in def_ssh.before:
        ep_r6_config()
    elif "EdgeRouter Lite" in def_ssh.before:
        erlite_3_config()
    elif "EdgeRouter PoE" in def_ssh.before:
        erpoe_5_config()
    elif "EdgeRouter Pro" in def_ssh.before:
        er_pro8_config()
    elif "EdgePoint Router 8" in def_ssh.before:
        ep_r8_config()
    elif "EdgeRouter 4" in def_ssh.before:
        er_4_config()
    elif "EdgeRouter 6P" in def_ssh.before:
        er_6p_config()
    elif "EdgeRouter 12" in def_ssh.before:
        er_12_config()
    elif "EdgeRouter Infinity" in def_ssh.before:
        er_x_config()
    elif "EdgeRouter" in def_ssh.before:
        under_construction
    else:
        return 26
