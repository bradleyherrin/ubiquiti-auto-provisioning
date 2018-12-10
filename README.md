# Ubiquiti EdgeMax Auto-Provisioning
---

<p align="center"> This project is authored by Bradley Herrin and Josh Moore. </p>

*<p align="center"> THIS PROJECT IS UNFINISHED. DO NOT RUN IT IN ITS CURRENT STATE. DOING SO RISKS BRICKING YOUR EQUIPMENT</P>*

---

## About
*Warning: This project is unfinished. Do not run it in its current state. Doing so risks bricking your equpment.*

This goal of this project is to use Python to auto-provision Ubiquiti EdgeMax and AirMax products. As of right now the idea is for the workflow to be as follows:

1. Plug up a device with a default config into Linux PC. The device cannot be connected to the internet, but if your Linux PC has two interfaces, one can be on the internet and the other can be statically assigned. A Raspberry Pi 3 B+ is a great option since it has ethernet and WiFi.
2. The Linux PC will then provision the device. This saves time by eliminating the need for manually updating firmware and manually configuring repetitive things that are required for every install.
3. Remove the device from the auto-provisioning network. From here you have two options:
    * Rebox the equipment and stage it for pickup by the installer and perform final configuration remotely.
    * Stage the equipment to someone to do final configuration. This is helpful when discovery is done ahead of time by you or the customer and you know all the customer-exclusive information that needs to be added like IPs, VLANS, port assignments, etc.

## Setup
Minimum requirements for this project are a working Linux or Mac with a working TFTP server and a real or NAT IP on the 192.168.1.0/24 subnet. The real IP can be statically assigned or assigned through a static lease.

If you don't already have a spare PC available to you, I would suggest a Raspberry Pi 3 B+ or better.

All setup will be performed via the command-line (SSH, terminal, etc)

### Step 1
Make sure you are in the home directory.
```cd ~/
```
Clone this repository in your home directory.
```git clone https://github.com/bradleyherrin/ubiquiti-auto-provisioning.git
```
### Step 2
Edit the user variables with Nano (if you prefer Vim use that instead).
```sudo nano ~/ubiquiti-auto-provisioning/ubiquiti-auto-provision.py
```
#### User Variables
*Only edit the text INSIDE the double quotes.*

```linux_pc = "192.168.1.254"
```
Set this to the real/NAT IP of your PC initiating the script and hosting the TFTP server.

```firmware_path = "./tftp/firmware/"
```
This is the TFTP firmware path. You should only have one firmware file here for a given firmware platform type. Firmware filenames should be in their original form from UBNT.

```config_path = "./tftp/config/"
```
This is the TFTP config path. Config files should be named in the format found in the edgeswitch.py, edgerouter.py, and airmax.py dictionaries.

Save the file when you finish with 'ctrl+O' (just hit enter to use same filename) or Vim equivalent.

### Step 3
Your TFTP root should contain two subfolders, config and firmware. If they don't exist already, use the following commands to create them.
```mkdir [TFTP filepath]/config
```
```mkdir [TFTP filepath]/firmware
```

#### Configurations
As stated above, the filenames should match the dictionaries in edgeswitch.py, edgerouter.py, and airmax.py. The filetype depends on the device.
* Switch - *.cfg*
* Router - *under construction*
* AP - *under construction*

#### Firmware
Firmware should be downloaded directly from https://www.ubnt.com/download/. The filenames should remain completely unchanged. There should be no more than one firmware version per model type. This means "ES-eswh.v1.7.4..." and "ES-eswh.v1.8.1..." both cannot be located in the same folder

The easiest way to download the firmware is to copy the firmware's "Direct URL" from Ubiquiti's website and then use 'wget'. This will allow you to download it directly to the TFTP directory.

#### File Permissions Issues
Make sure that any files you add to your TFTP directory don't have any file permissions issues. You can fix any file permissions issues by running 'sudo chown -R nobody [TFTP filepath]' and 'sudo chmod -R 777 [TFTP filepath]'. Make sure to run these commands AFTER you add any config or firmware files.

### Step 4
Make 'ubiquiti-auto-provision.py' executable.
```sudo chmod u+x ~/ubiquiti-auto-provisioning/ubiquiti-auto-provision.py
```

After this you have two options, run the file manually or set up automation with a cron job.

#### Manual Execution
Manually execute the file using './ubiquiti-auto-provision.py' while within the ~/ubiquiti-auto-provisioning/ directory. Otherwise you will need to execute the file with './path/to/ubiquiti-auto-provisioning/ubiquiti-auto-provision.py'.

#### Automated Execution
Automating this file with a cron job makes this script able to be utilized by anyone, regardless of skill. Someone, a warehouse worker for example, can just hook the equipment up to the auto-provisioning network and come back later to rebox it. At that point the equipment is on the shelf ready to go and requires no work from a technician other than physical installation. Finalization of the configuration can be performed by a Network Engineer remotely.

```
Automated Execution is under construction
```

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
* ES-5XP
* ES-8XP
* ES-10X
* ES-10XP
* ES-16XP
* ES-16-XG

### Airmax
Under construction

## Credits

### Authors
Bradley Herrin
Josh Moore

### Python Modules

#### Third Party
Pexpect (https://pexpect.readthedocs.io/en/latest/index.html)

#### Python Standard Library
Subprocess (https://docs.python.org/2/library/subprocess.html)
Time (https://docs.python.org/2/library/time.html)
