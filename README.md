# DuraFET UDA System Monitor

## Introduction
This script is a Python interpretation of the methods in "Advancing Ocean Acidification Biology Using Durafet® pH Electrodes",
which was published in [Frontiers in Marine Science (2017)](https://www.frontiersin.org/articles/10.3389/fmars.2017.00321/full).The main purpose of this project is to provide an alternative to the use of the commercially available, proprietary LabView Software and instead use a tool that is ubiquitous, free, and open-source. 

This adaptation is conducted under the original [Attribution 4.0 International CC](https://creativecommons.org/licenses/by/4.0/) of the main article, while fully acknowledging that this work would not have been possible without the prior work of Kapsenberg et al. 

## System Requirements

### Hardware Requirements

* **Computer**: This can be run on any hardware that can run Python 3, but was tested on a Thinkpad A475 running Windows 10. The computer must also have a way of connecting to the same network as the UDA's (e.g. ethernet port for hardline connection). If you are setting up a local hardwired network for the UDA's, having both wifi and ethernet capabilities on the computer will allow you to still access the internet on a wifi network at the same time as running the UDA's off of the ethernet port.

* **UDA's**: This software can be used to monitor any TCP/Modbus communications, but has been written with the Honeywell UDA2182 in mind (IEEE 32-bit floating point big endian). Our units were fitted with the communications card, as well as two pH cards for reading directly from DuraFET III probes. This UDA configuration is identical to that described in Kapsenberg et al (2017). 

* **Networking**: As detailed in the reference paper, the computer can be connected directly to a single UDA with a crossover Ethernet cable. However, with most computers having only one ethernet port, connecting multiple UDA's could easily be accomplished using any ethernet switch. 

### Software Requirements

* **Computer**: This can be run on any operating system, but was run using Windows 10. Choose the operating system where you are most comfortable working with network configuration. 

* **Python**: This code is written for Python 3, and will not run on Python 2. Dependencies are stated at the beginning of the main script, and can be simply installed using `pip` or `easy_install` before running the scripts.



## Setup

1. Your computer should be set up with a static IP address under IPv4. You'll want to set this up with the same network address (first 2 sets of numbers) as the UDA if you want to also have the computer hooked up to wifi. Make sure that this is different from the network address on the IP address issued by your wireless network (`ipconfig` on windows, `ifconfig` on Mac/Linux). Given the default UDA IP address of `192.168.1.254`, I set our computer up to `192.168.1.50`. I found that turning of IPv6 can help as well, but may not be necessary. Subnet mask....

2. UDA's can be kept with default settings, save for assigning unique IP addresses.

3. After hooking up UDA's to the network, test the IP addresses by pinging them from the computer (`ping 192.168.1.254` for Windows/Mac/Linux, replace IP address with that of each UDA). You should get a response from every UDA's IP before starting up the script - otherwise you have a network connection problem. 

4. Run script, currently set up for a single UDA and set up to output a single set of pH/temperature. The instructions for editing the UDA variables are in the script. 

## To Do: 

* Continue writing "setup" portion of `readme`
* Connect to multiple UDA's (confirm in code)
* Output to a .txt file every x minutes
* Tweet, Slack, or Email the daily values, along with a plot



### Primary work cited: 

* Kapsenberg Lydia, Bockmon Emily E., Bresnahan Philip J., Kroeker Kristy J., Gattuso Jean-Pierre, Martz Todd R. "Advancing Ocean Acidification Biology Using Durafet® pH Electrodes". Frontiers in Marine Science, vol.4 (2017). DOI=10.3389/fmars.2017.00321    
	
