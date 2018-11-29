# switch_config.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Use this section to build your own
# configs using tn.sendline and tn.expect.
# Currently all this does is add a new
# user, remove the default user "ubnt",
# set up UNMS, and then close the Telnet
# session. The idea is that you would build
# out configs for each model you need to
# provision. Scroll down to see the logic
# used to check for different switch models.

# Imports
import pexpect

# Variables
switch = "192.168.1.2"
switch_tftp = "copy tftp://192.168.1.199/ES-eswh.v1.7.4.5075842.stk backup"
creds = "ubnt"
new_user = "CHANGE ME"
new_pass = "CHANGE ME"
priv = " level 15"
unms_key = "YOUR KEY HERE"
tn = pexpect.spawn("telnet " + switch)
tn_new = pexpect.spawn("telnet " + switch)

# Functions
def switch_default_login():
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(":")
    tn.sendline(creds)
    tn.expect(">")
    tn.sendline("enable")
    tn.expect(":")
    tn.sendline(creds)
    tn.expect("#")

def switch_new_login():
    tn.expect(":")
    tn.sendline(new_user)
    tn.expect(":")
    tn.sendline(new_pass)
    tn.expect(">")
    tn.sendline("enable")
    tn.expect(":")
    tn.sendline(new_pass)
    tn.expect("#")
    tn.sendline("configure")
    tn.expect("#")

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
    tn.close()

def switch8():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch16():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch24():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch48():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch5():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch10():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch12():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switchS16():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

def switch16XG():
    tn.sendline("username " + new_user + "password " + new_pass + priv)
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")
    switch_new_login()
    tn.sendline("no username ubnt")
    tn.expect("#")
    tn.sendline("service unms key" + unms_key)
    tn.expect("#")
    tn.sendline("service unms")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect("#")
    tn.sendline("write memory")
    tn.expect("(y/n)")
    tn.sendline("y")
    tn.expect("#")
    tn.sendline("exit")
    tn.expect(">")
    tn.sendline("exit")

# Here is the logic that will check for which config to serve.
# Keep in mind that the order is important. For example, the
# ES-16-XG comes before ES-16 switch to prevent the switch16()
# function from being pushed to an ES-16-XG.

def switch_config():
    switch_default_login()
    tn.sendline("show version")
    tn.expect("Serial")
    if "ES-8" in tn.before:
        switch8()
    elif "ES-16-XG" in tn.before:
        switch16XG()
    elif "ES-16" in tn.before:
        switch16()
    elif "ES-24" in tn.before:
        switch24()
    elif "ES-48" in tn.before:
        switch48()
    elif "ES-5XP" in tn.before:
        switch5()
    elif "ES-10" in tn.before:
        switch10()
    elif "ES-12" in tn.before:
        switch12()
    elif "EP-S16" in tn.before:
        switchS16()
    else:
        return 26
