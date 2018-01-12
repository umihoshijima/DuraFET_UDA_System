from pymodbus.client.sync import ModbusTcpClient
import struct # used for the hex stuff
import time  # used to pause script
from datetime import datetime # used for current time
import csv # for writing csv files: 
# following the pandas tutorial here: https://pandas.pydata.org/pandas-docs/stable/10min.html#min

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
# https://github.com/riptideio/pymodbus

# connect to our modbus client
client1 = ModbusTcpClient('192.168.1.254')
time.sleep(1)

# Much thanks to Stack Overflow commenter Nathan for this: 
#https://stackoverflow.com/questions/48217264/python-converting-two-sequential-2-byte-registers-4-bytes-into-ieee-floating
def bigIntToFloat(bigIntlist):
    pair = []
    for bigInt in bigIntlist:
        pair.append(bytes.fromhex(format(bigInt, 'x')))
        if len(pair) == 2:
            yield struct.unpack('>f', b''.join(pair))[0]
            pair = []



# These are the bytes that we want, the first 8:
a = client1.read_input_registers(0,8)
# Pull the registers off of them
b = a.registers
# this converts them into 32-bit floats
dat = bigIntToFloat(b)

# Pull out of the dat object, last number is decimal places. 
pH_1 = round(next(dat),3)
pH_2 = round(next(dat),3)
temp_1 = round(next(dat),2)
temp_2 = round(next(dat),2)

# Used this doc here: https://docs.python.org/3.5/tutorial/inputoutput.html

# got current datetime form this answer:
# https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

print( 'Probe 1: pH of {0} and temperature of {1} C'.format(pH_1, temp_1))
print( 'Probe 2: pH of {0} and temperature of {1} C'.format(pH_2, temp_2))


### Here below is untested.
 
#df = pd.dataframe(


client1.close()
