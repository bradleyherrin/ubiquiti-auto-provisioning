#!/usr/bin/env python

# ubiquiti-auto-provision.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeMax and AirMax products.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

# Imports
import pexpect,subprocess,time,edgeswitch,edgerouter

# Variables
pinging = True
ping = "ping -c 5 "
ping_match = " | grep -c 'bytes from' | grep 5"
linux_pc = "192.168.1.199"
er_x = "EdgeRouter X"
er_x_sfp = "EdgeRouter X SFP"
er_10x = "EdgeRouter 10X"
ep_r6 = "EdgePoint Router 6"
erlite_3 = "EdgeRouter Lite"
erpoe_5 = "EdgeRouter PoE"
er_pro8 = "EdgeRouter Pro"
er_8 = "EdgeRouter"
ep_r8 = "EdgePoint Router 8"
er_4 = "EdgeRouter 4"
er_6p = "EdgeRouter 6P"
er_12 = "EdgeRouter 12"
er_8_xg = "EdgeRouter Infinity"
run_boot = "(running image) (default boot)"
trans_success = "File transfer operation completed successfully.\n".center(45)

# Welcome message
print("---------------------------------------------".center(45))
print("Welcome to the Ubiquiti EdgeMax and AirMax".center(45))
print("Auto-Provisioning Application".center(45))
print("by Bradley Herrin and Josh Moore".center(45))
print("---------------------------------------------".center(45))

# Ping check
while pinging:
    if subprocess.call(ping + edgerouter.router + ping_match, shell=True) == 0:
        # Check router version
        edgerouter.default_login()
        edgerouter.version_check()
        if er_x or er_x_sfp or er_10x or ep_r6 in edgerouter.ssh1.before:
            edgerouter.firmware_check()
            if "1.10.8." and run_boot in edgerouter.ssh1.before:
                # User message
                edgerouter.configuring_um()
                # Configure router
                edgerouter.config()
                if edgerouter.config() == 26:
                    # User message
                    edgerouter.model_not_found_um()
                    break
                else:
                    # User message
                    edgerouter.configured_successfully_um()
                    break
            else:
                # User message
                edgerouter.updating_firmware_um()
                # Update router firmware
                edgerouter.e50_fw_update()
                if "success" in edgerouter.ssh1.before:
                    print(trans_success)
                    # User message
                    edgerouter.active_reboot_um()
                    # Set active and reboot
                    edgerouter.set_active_reboot()
                    time.sleep(300)
                else:
                    print("File transfer failed. Please try again.".center(45))
                    break
        elif erlite_3 or erpoe_5 in edgerouter.ssh1.before:
            edgerouter.firmware_check()
            if "1.10.8." and run_boot in edgerouter.ssh1.before:
                # User message
                edgerouter.configuring_um()
                # Configure router
                edgerouter.config()
                if edgerouter.config() == 26:
                    # User message
                    edgerouter.model_not_found_um()
                    break
                else:
                    # User message
                    edgerouter.configured_successfully_um()
                    break
            else:
                # User message
                edgerouter.updating_firmware_um()
                # Update router firmware
                edgerouter.e100_fw_update()
                if "success" in edgerouter.ssh1.before:
                    print(trans_success)
                    # User message
                    edgerouter.active_reboot_um()
                    # Set active and reboot
                    edgerouter.set_active_reboot()
                    time.sleep(300)
                else:
                    print("File transfer failed. Please try again.".center(45))
                    break
        elif er_pro8 or er_8 or ep_r8 in edgerouter.ssh1.before:
            edgerouter.firmware_check()
            if "1.10.8." and run_boot in edgerouter.ssh1.before:
                # User message
                edgerouter.configuring_um()
                # Configure router
                edgerouter.config()
                if edgerouter.config() == 26:
                    # User message
                    edgerouter.model_not_found_um()
                    break
                else:
                    # User message
                    edgerouter.configured_successfully_um()
                    break
            else:
                # User message
                edgerouter.updating_firmware_um()
                # Update router firmware
                edgerouter.e200_fw_update()
                if "success" in edgerouter.ssh1.before:
                    print(trans_success)
                    # User message
                    edgerouter.active_reboot_um()
                    # Set active and reboot
                    edgerouter.set_active_reboot()
                    time.sleep(300)
                else:
                    print("File transfer failed. Please try again.".center(45))
                    break
        elif er_4 or er_6p or er_12 in edgerouter.ssh1.before:
            edgerouter.firmware_check()
            if "1.10.8." and run_boot in edgerouter.ssh1.before:
                # User message
                edgerouter.configuring_um()
                # Configure router
                edgerouter.config()
                if edgerouter.config() == 26:
                    # User message
                    edgerouter.model_not_found_um()
                    break
                else:
                    # User message
                    edgerouter.configured_successfully_um()
                    break
            else:
                # User message
                edgerouter.updating_firmware_um()
                # Update router firmware
                edgerouter.e300_fw_update()
                if "success" in edgerouter.ssh1.before:
                    print(trans_success)
                    # User message
                    edgerouter.active_reboot_um()
                    # Set active and reboot
                    edgerouter.set_active_reboot()
                    time.sleep(300)
                else:
                    print("File transfer failed. Please try again.".center(45))
                    break
        elif er_8_xg in edgerouter.ssh1.before:
            edgerouter.firmware_check()
            if "1.10.8." and run_boot in edgerouter.ssh1.before:
                # User message
                edgerouter.configuring_um()
                # Configure router
                edgerouter.config()
                if edgerouter.config() == 26:
                    # User message
                    edgerouter.model_not_found_um()
                    break
                else:
                    # User message
                    edgerouter.configured_successfully_um()
                    break
            else:
                # User message
                edgerouter.updating_firmware_um()
                # Update router firmware
                edgerouter.e1000_fw_update()
                if "success" in edgerouter.ssh1.before:
                    print(trans_success)
                    # User message
                    edgerouter.active_reboot_um()
                    # Set active and reboot
                    edgerouter.set_active_reboot()
                    time.sleep(300)
                else:
                    print("File transfer failed. Please try again.".center(45))
                    break
        else:
            edgerouter.model_not_found_um()
            break
    elif subprocess.call(ping+edgeswitch.switch+ping_match, shell=True) == 0:
        # Check switch firmware
        edgeswitch.default_login()
        edgeswitch.add_new_user()
        edgeswitch.firmware_check()
        if "active  *1.7.4.5075842" in edgeswitch.tn.before:
            # User message
            edgeswitch.configuring_um()
            # Configure switch
            edgeswitch.config()
            if edgeswitch.config() == 26:
                # User message
                edgeswitch.model_not_found_um()
                break
            else:
                # User message
                edgeswitch.configured_successfully_um()
                break
        elif "backup   1.7.4.5075842" in edgeswitch.tn.before:
            # User message
            edgeswitch.active_reboot_um()
            # Set active and reboot
            edgeswitch.set_active_reboot()
            time.sleep(300)
        else:
            # User message
            edgeswitch.updating_firmware_um()
            # Update switch firmware
            edgeswitch.update_firmware()
            if "success" in edgeswitch.tn.before:
                print(trans_success)
                # User message
                edgeswitch.active_reboot_um()
                # Set active and reboot
                edgeswitch.set_active_reboot()
                time.sleep(300)
            else:
                print("File transfer failed. Please try again.".center(45))
                break
    else:
        # No devices found
        print('No devices found.')
        break
