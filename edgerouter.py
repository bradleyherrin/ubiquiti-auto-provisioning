# edgerouter.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect
import time
connection = ""
firmware_file = ""

# Device models dictionary
router_models = {
    'EdgeRouter X': {
        'firmware': 'e50'
    },
    'EdgePoint R6': {
        'firmware': 'e50'
    },
    'EdgeRouter 10X': {
        'firmware': 'e50'
    },
    'EdgeRouter Lite': {
        'firmware': 'e100'
    },
    'EdgeRouter PoE': {
        'firmware': 'e100'
    },
    'EdgePoint R8': {
        'firmware': 'e200'
    },
    'EdgeRouter Pro': {
        'firmware': 'e200'
    },
    'EdgeRouter 4': {
        'firmware': 'e300'
    },
    'EdgeRouter 6P': {
        'firmware': 'e300'
    },
    'EdgeRouter 12': {
        'firmware': 'e300'
    },
    'EdgeRouter Infinity': {
        'firmware': 'e1000'
    }
}


# Functions
def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring router...".center(45))
    print("---------------------------------------------".center(45))


def found_login_um(login_type):
    print("---------------------------------------------".center(45))
    print("Found router, logging in with SSH...").center(45)
    print("---------------------------------------------".center(45))


def router_model_um(model):
    print("---------------------------------------------".center(45))
    print("Router model is " + model + ".").center(45)
    print("---------------------------------------------".center(45))


def latest_router_firmware_um(firmware):
    print("---------------------------------------------".center(45))
    print("Latest switch firmware is " + firmware + ".").center(45)
    print("Checking if upgrade is needed...").center(45)
    print("---------------------------------------------".center(45))


def no_upgrade_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgrade not needed.").center(45)
    print("---------------------------------------------".center(45))


def upgrade_failed_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgrade failed.").center(45)
    print("---------------------------------------------".center(45))


def model_not_found_um():
    print("---------------------------------------------".center(45))
    print("Router model not found.").center(45)
    print("Router was not configured.").center(45)
    print("---------------------------------------------".center(45))


def configured_successfully_um():
    print("---------------------------------------------".center(45))
    print("Router configured successfully!".center(45))
    print("---------------------------------------------".center(45))


def active_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgraded successfully!").center(45)
    print("Setting backup as active...".center(45))
    print("---------------------------------------------".center(45))


def updating_firmware_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgrade needed.").center(45)
    print("Upgrading router firmware...").center(45)
    print("---------------------------------------------".center(45))


def default_login(creds, router):
    global connection
    pexpect.run("ssh-keygen -R " + router + " >/dev/null")
    connection = pexpect.spawn("ssh " + creds + "@" + router)
    connection.expect("(yes/no)? ")
    connection.sendline("yes")
    connection.expect("password: ")
    connection.sendline(creds)
    connection.expect("$")


def firmware_check():
    connection.expect("$")
    connection.sendline("show version")
    connection.expect("Build ID:")


def update_firmware(linux_pc):
    connection.sendline("delete system image")
    connection.expect("(Yes/No)")
    connection.sendline("yes")
    connection.expect("$")
    connection.sendline("add system image tftp://" + linux_pc + "/firmware/" + firmware_file)
    connection.expect("(Yes/No)")
    connection.sendline("yes")


def set_active():
    connection.sendline("set system image default-boot")
    connection.expect("$")
    connection.sendline("reboot")
    connection.expect("[confirm]")
    connection.sendline("y")


def latest_router_firmware(firmware_path, model):
    global firmware_file
    firmware = router_models.get(model, {}).get('firmware')
    firmware_file = pexpect.run("find " + firmware_path + " -name '*" + firmware + "*' -printf '%f'")
    split_version = firmware_file.rsplit(firmware + ".v")
    switch_version = split_version[1].split('.tar')
    return switch_version[0]


def switch_model():
    connection.expect("$")
    connection.sendline("show version")
    connection.expect("HW S/N")
    for model in router_models:
        if model in connection.before:
            return model
    return 26


def config(linux_pc, model):
    connection.sendline("configure")
    connection.expect("#")
    connection.sendline("load tftp://"+linux_pc+"/config/"+model+".boot")
    connection.expect("(y/n)")
    connection.sendline("y")
    connection.expect("successfully.")
    connection.sendline("commit ; save")
    connection.expect("successful")
    connection.sendline("exit")
    connection.expect("$")
    connection.sendline("reboot")
    connection.expect("[confirm]")
    connection.sendline("y")
