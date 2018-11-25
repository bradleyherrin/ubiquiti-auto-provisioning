# ubiquiti-auto-provisioning

---

<p align="center">
  <img src="https://bradleyherrin.me/images/BH_Logo_black_small.png" />
</p>
<p align="center"> This project is authored by Bradley Herrin. </p>

---

## About
This goal of this project is to use Python to auto-provision EdgeRouters and EdgeSwitches. In this case, auto-provisioning includes updating the firmware followed by pushing a base configuration. As of right now the idea is for the workflow to be as follows:

1. Plug up new EdgeMax device into the auto-provisioning network that consists of a Linux PC and a switch.
2. The Linux box will then provision the device with things that have been determined to be required for all installations.
    * Examples include UNMS keys, an admin user account, deletion of the default ubnt/ubnt account, etc
3. Remove the device from the auto-provisioning network. From here you have two options:
    * Rebox the equipment and stage it for pickup by the installer and perform final configuration remotely. The caveat here is that you need to make sure you have remote access. In the case of EdgeRouters, UNMS will be the backdoor to finish up remotely. In the case of EdgeSwitches, either make sure you have Layer 2 access or install an ER-X along side the switch for remote configuration. The ER-X can be left or picked up at a later date.
    * Stage the equipment to someone to do final configuration. This is helpful when discovery is done ahead of time by you or the customer and you know all the customer-exclusive information that needs to be added like IPs, VLANS, port assignments, etc.

## Technical Stuff

The first step in the process is determining device type. This will be done using ping. The Linux PC will ping the default IPs for each device type. This will tell the Python script which firmware and configuration to push.

EdgeMax devices have the following default IPs.
* EdgeRouters - 192.168.1.1/24
* EdgeSwitches - 192.168.1.2/24

This means the Linux PC will need to be configured with a static IP on the same subnet.

After determining device type through ping, the Linux PC will then access the device through either SSH (EdgeRouters) or Telnet (EdgeSwitches) and a firmware check will be performed. If a certain version isn't detected The firmware will be updated via a TFTP server running on the same Linux PC. Once the result of the firmware check is equal to the required version, the base configuration will be pushed to the device.

Now, in the case of my department at work, the device is ready to have customer-exclusive information configured in the next stage.
