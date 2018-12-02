# Ubiquiti EdgeMax Auto-Provisioning

---

<p align="center">
  <img src="https://bradleyherrin.me/images/BH_Logo_black_small.png" />
</p>
<p align="center"> This project is authored by Bradley Herrin and Josh Moore. </p>

---

## About
This goal of this project is to use Python to auto-provision Ubiquiti EdgeMax and AirMax products. In this case, auto-provisioning includes updating the firmware followed by pushing a base configuration. As of right now the idea is for the workflow to be as follows:

1. Plug up a device with a default config into Linux PC. The device cannot be connected to the internet, but if your Linux PC has two interfaces, one can be on the internet and the other can be statically assigned. A Raspberry Pi 3 B+ is a great option since it has ethernet and WiFi.
2. The Linux PC will then provision the device. This saves time by eliminating the need for manually updating firmware and manually configuring repetitive things that are required for every install.
3. Remove the device from the auto-provisioning network. From here you have two options:
    * Rebox the equipment and stage it for pickup by the installer and perform final configuration remotely.
    * Stage the equipment to someone to do final configuration. This is helpful when discovery is done ahead of time by you or the customer and you know all the customer-exclusive information that needs to be added like IPs, VLANS, port assignments, etc.

## Technical Stuff

The first step in the process is determining device type. This will be done using ping. The Linux PC will ping the default IPs for each device type. This will tell the Python script which firmware and configuration to push.

EdgeMax devices have the following default IPs.
* EdgeRouters - 192.168.1.1/24
* EdgeSwitches - 192.168.1.2/24

AirMax devices use 192.168.1.20/24 as their default IP.

This means the Linux PC will need to be configured with a static IP on the same 192.168.1.0/24 subnet.

After determining device type through ping, the Linux PC will then access the device through either SSH or Telnet and a firmware check will be performed. If a certain version isn't detected The firmware will be updated via a TFTP server running on the same Linux PC. Once the result of the firmware check is equal to the required version, the base configuration will be pushed to the device.

## Compatibility

### EdgeRouters

Under construction.

### EdgeSwitches

The following is a list of compatible devices.
* ES-8-150W
* ES-12F
* ES-16-150W
* EP-S16
* ES-24-LITE
* ES-24-250W
* ES-24-500W
* ES-48-LITE
* ES-48-500W
* ES-48-750W

The following is a list of incompatible devices. As these devices become compatible they will be moved to the list above.
* ES-10X
* ES-10XP
* ES-16-XG
