# DuraFET UDA System Monitor

## Introduction
This script is a Python interpretation of the methods in "Advancing Ocean Acidification Biology Using Durafet® pH Electrodes",
which was published in [Frontiers in Marine Science (2017)](https://www.frontiersin.org/articles/10.3389/fmars.2017.00321/full).The main purpose of this project is to provide an alternative to the use of the commercially available, proprietary LabView Software and instead use a tool that is ubiquitous, free, and open-source. 

This adaptation is conducted under the original [Attribution 4.0 International CC](https://creativecommons.org/licenses/by/4.0/) of the main article, while fully acknowledging that this work would not have been possible without the prior work of Kapsenberg et al. 

## System Requirements

### Hardware Requirements

* **Computer**: This can be run on any hardware that can run Python 3, but was tested on a Thinkpad A475 running Windows 10. The computer must also have an ethernet port, or some other way of connecting to the same network as the UDA's. 

* **UDA's**: This software can be used to monitor any TCP/Modbus communications, but has been written with the Honeywell UDA2182 in mind. Our units were fitted with the Communications card, as well as two pH cards for reading directly from DuraFET III probes. This UDA configuration is identical to that described in Kapsenberg et al (2017). 

* **Networking**: As detailed in the reference paper, the computer can be connected directly to a single UDA with a crossover Ethernet cable. However, with most computers having only one ethernet port, connecting multiple UDA's could easily be accomplished using any ethernet switch. 

### Software Requirements

* **Computer**: This can be run on any operating system, but was run using Windows 10. Choose the operating system where you are most comfortable working with network configuration. 

* **Python**: This code is written for Python 3, and will not run on Python 2. Dependencies are stated at the beginning of the main script, and can be simply installed using `pip` or `easy_install` before running the scripts.

## To Do: 

* Continue writing "setup" portion of `readme`
* Connect to multiple UDA's (confirm in code)
* Output to a .txt file every x minutes
* Tweet, Slack, or Email the daily values, along with a plot




### Primary work cited: 

* Kapsenberg Lydia, Bockmon Emily E., Bresnahan Philip J., Kroeker Kristy J., Gattuso Jean-Pierre, Martz Todd R. "Advancing Ocean Acidification Biology Using Durafet® pH Electrodes". Frontiers in Marine Science, vol.4 (2017). DOI=10.3389/fmars.2017.00321    
	
