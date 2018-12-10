# airmax.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

import pexpect
import time
connection = ""
firmware_connection = ""

# Device models dictionary
airmax_models = {
    'WA': {
        'firmware': 'WA'
    },
    'XC': {
        'firmware': 'XC'
    },
    'XW': {
        'firmware': 'XW'
    }
}


# Functions
def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring airmax...".center(45))
    print("---------------------------------------------".center(45))


def found_login_um():
    print("---------------------------------------------".center(45))
    print("Found airmax, logging in with SSH...".center(45))
    print("---------------------------------------------".center(45))


def airmax_model_um(model):
    print("---------------------------------------------".center(45))
    print("airmax platform is " + model + ".").center(45)
    print("---------------------------------------------".center(45))


def latest_airmax_firmware_um(firmware):
    print("---------------------------------------------".center(45))
    print("Latest airmax firmware is " + firmware + ".").center(45)
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
    print("airmax model not found.").center(45)
    print("airmax was not configured.").center(45)
    print("---------------------------------------------".center(45))


def configured_successfully_um():
    print("---------------------------------------------".center(45))
    print("airmax configured successfully!".center(45))
    print("---------------------------------------------".center(45))


def active_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgraded successfully!").center(45)
    print("Setting backup as active...".center(45))
    print("---------------------------------------------".center(45))


def updating_firmware_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgrade needed.").center(45)
    print("Upgrading airmax firmware...").center(45)
    print("---------------------------------------------".center(45))


def default_login(creds, ap):
    global connection
    pexpect.run("ssh-keygen -R " + ap)
    connection = pexpect.spawn("ssh " + creds + "@" + ap + " > /dev/null")
    connection.expect("(yes/no)? ")
    connection.sendline("yes")
    connection.expect("password: ")
    connection.sendline(creds)
    connection.expect("#")


def firmware_check():
    connection.sendline("cat /etc/version")
    connection.expect("#")


def update_firmware(ap, creds, firmware, firmware_path):
    global firmware_connection
    firmware_connection = pexpect.spawn("scp -o StrictHostKeyChecking=no " + firmware_path + firmware + " " + creds + "@" + ap + ":/tmp/fwupdate.bin")
    firmware_connection.expect("password: ")
    firmware_connection.sendline(creds)
    time.sleep(240)


def set_active():
    connection.sendline("/sbin/fwupdate -m")
    connection.expect("update")


def latest_airmax_firmware(firmware_path, model):
    firmware = airmax_models.get(model, {}).get('firmware')
    firmware_file = pexpect.run("find " + firmware_path + " -name '*" + firmware + "*' -printf '%f\n'")
    airmax_version = firmware_file.rsplit(firmware + ".v")
    return airmax_version[0]


def airmax_model():
    connection.sendline("cat /etc/version")
    connection.expect("#")
    for model in airmax_models:
        if model in connection.before:
            return model
    return 26


def config(ap, model, config_path):
    global firmware_connection
    firmware_connection = pexpect.spawn("scp -o StrictHostKeyChecking=no " + config_path + model + ".cfg " + creds + "@" + ap + ":/tmp/system.cfg")
    firmware_connection.expect("password: ")
    firmware_connection.sendline(creds)
    time.sleep(60)
    connection.sendline("cfgmtd -f /tmp/system.cfg -w")
    connection.expect("#")
    connection.sendline("/usr/etc/rc.d/rc.softrestart save")
    connection.expect("#")