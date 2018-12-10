# edgeswitch.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

import pexpect
import time
connection = ""
firmware_file = ""

# Device models dictionary
switch_models = {
    'ES-8': {
        'firmware': 'ES-eswh'
    },
    'ES-12': {
        'firmware': 'ES-eswh'
    },
    'ES-16-150W': {
        'firmware': 'ES-eswh'
    },
    'ES-16-XG': {
        'firmware': 'ES-esgh'
    },
    'ES-24': {
        'firmware': 'ES-eswh'
    },
    'ES-48': {
        'firmware': 'ES-eswh'
    },
    'EP-S16': {
        'firmware': 'ES-eswh'
    }
}


# Functions
def configuring_um():
    print("---------------------------------------------".center(45))
    print("Configuring switch...".center(45))
    print("---------------------------------------------".center(45))


def found_login_um(login_type):
    print("---------------------------------------------".center(45))
    print("Found switch, logging in with " + login_type + "...").center(45)
    print("---------------------------------------------".center(45))


def switch_model_um(model):
    print("---------------------------------------------".center(45))
    print("Switch model is " + model + ".").center(45)
    print("---------------------------------------------".center(45))


def latest_switch_firmware_um(firmware):
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
    print("Switch model not found.").center(45)
    print("Switch was not configured.").center(45)
    print("---------------------------------------------".center(45))


def configured_successfully_um():
    print("---------------------------------------------".center(45))
    print("Switch configured successfully!".center(45))
    print("---------------------------------------------".center(45))


def active_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgraded successfully!").center(45)
    print("Setting backup as active...".center(45))
    print("---------------------------------------------".center(45))


def updating_firmware_um():
    print("---------------------------------------------".center(45))
    print("Firmware upgrade needed.").center(45)
    print("Upgrading switch firmware...").center(45)
    print("---------------------------------------------".center(45))


def default_login(telnet_connection, creds, switch):
    global connection
    if telnet_connection == True:
        connection = pexpect.spawn("telnet " + switch)
        connection.expect("User:")
        connection.sendline(creds)
        connection.expect("Password:")
        connection.sendline(creds)
        connection.expect(">")
        connection.sendline("enable")
        connection.expect("Password:")
        connection.sendline(creds)
        connection.expect("#")
    elif telnet_connection == False:
        pexpect.run("ssh-keygen -R " + switch + " >/dev/null")
        connection = pexpect.spawn("ssh " + creds + "@" + switch)
        connection.expect("(yes/no)? ")
        connection.sendline("yes")
        connection.expect("password: ")
        connection.sendline(creds)
        connection.expect(">")
        connection.sendline("enable")
        connection.expect("Password:")
        connection.sendline(creds)
        connection.expect("#")


def firmware_check():
    connection.sendline("show bootvar")
    connection.expect("Current")


def update_firmware(linux_pc):
    connection.sendline("copy tftp://" + linux_pc + "/firmware/" + firmware_file + " backup")
    print connection.after
    connection.expect("start? ")
    connection.sendline("y")
    time.sleep(240)
    connection.expect("lly.")


def set_active():
    connection.sendline("boot system backup")
    connection.expect("#")


def latest_switch_firmware(hardcoded_switch_version, firmware_path, model):
    global firmware_file
    firmware = switch_models.get(model, {}).get('firmware')
    if firmware_path and not hardcoded_switch_version:
        firmware_file = pexpect.run("find " + firmware_path + " -name '*" + firmware + "*' -printf '%f'")
        split_version = firmware_file.rsplit(firmware + ".v")
        switch_version = split_version[1].split('.stk')
        return switch_version[0]
    else:
        return hardcoded_switch_version


def switch_model():
    connection.sendline("show version")
    connection.expect("Serial")
    for model in switch_models:
        if model in connection.before:
            return model
    return 26


def config(linux_pc, model):
    connection.sendline("copy tftp://" + linux_pc + "/config/" + model + ".cfg nvram:startup-config")
    connection.expect("(y/n)")
    connection.sendline("y")
    connection.expect("successfully.")
    connection.sendline("reload")
    connection.expect("(y/n)")
    connection.sendline("y")