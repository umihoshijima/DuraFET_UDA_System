##### These are the variables you can change:

DELAY_MIN = 1 #TIME interval, in minutes.
UDA_1_IP = '192.168.1.254'  #IP address of a single UDA.
FILE_NAME = 'pH_data_loadedpHOx_20180117.csv' # This is the name of the file.
# Note that this makes a file in the same folder as the script.
# If this is not desired, use relative or absolute paths under FILE_NAME.


##########################

# Import all dependencies. Use pip or easy_install first if these don't work.
from pymodbus.client.sync import ModbusTcpClient
import struct # used for the hex stuff
import time  # used to pause script
from datetime import datetime # used for current time
import csv # for writing csv files: 
# following the pandas tutorial here: https://pandas.pydata.org/pandas-docs/stable/10min.html#min
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#
# Much thanks to Stack Overflow commenter Nathan for this: 
#https://stackoverflow.com/questions/48217264/python-converting-two-sequential-2-byte-registers-4-bytes-into-ieee-floating

def bigIntToFloat(bigIntlist):
    pair = []
    for bigInt in bigIntlist:
        num = format(bigInt,'x')
        while len(num)<4:
            num = "0"+num  # Without preceding 0's, throwing errors.
        pair.append(bytes.fromhex(num))
        if len(pair) == 2:
            yield struct.unpack('>f', b''.join(pair))[0]
            pair = []





fields = ['time', 'pH_1', 'temp_1', 'pH_2', 'temp_2']
with open(FILE_NAME, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)



while True:
    time_current = datetime.now()
    # Refer to this link for modbus resources.
    # https://github.com/riptideio/pymodbus
    # connect to our modbus client
    client1 = ModbusTcpClient(UDA_1_IP)
    time.sleep(1) # just to make sure things are well-marinated.

	# These are the bytes that we want, the first 8:
    a = client1.read_input_registers(0,8).registers
	# Pull the registers off of them

	# this converts them into 32-bit floats
    dat = bigIntToFloat(a)
	
	# Pull out of the dat object, last number is decimal places. 
    pH_1 = next(dat)
    pH_2 = next(dat)
    temp_1 = next(dat)
    temp_2 = next(dat)
	

	# Used this doc here: https://docs.python.org/3.5/tutorial/inputoutput.html

	# got current datetime form this answer:
	# https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python

    print(time_current.strftime('%Y-%m-%d %H:%M:%S'))

    print( 'Probe 1: pH of {0} and temperature of {1} C'.format(round(pH_1, 2), round(temp_1, 3)))
    print( 'Probe 2: pH of {0} and temperature of {1} C'.format(round(pH_2, 2), round(temp_2, 3)))


    fields = [time_current.strftime('%Y-%m-%d %H:%M:%S'), pH_1, temp_1, pH_2, temp_2]
    with open(FILE_NAME, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

	# close clients
    client1.close()
    time.sleep( ((60 - time.localtime().tm_min - (time.localtime().tm_sec/60))%DELAY_MIN)*60) # run every 30 seconds
