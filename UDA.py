from pymodbus.client.sync import ModbusTcpClient
import struct # used for the hex stuff
import time  # used to pause script
from datetime import datetime # used for current time
import csv # for writing csv files: 
# following the pandas tutorial here: https://pandas.pydata.org/pandas-docs/stable/10min.html#min

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# https://github.com/riptideio/pymodbus

# Much thanks to Stack Overflow commenter Nathan for this: 
#https://stackoverflow.com/questions/48217264/python-converting-two-sequential-2-byte-registers-4-bytes-into-ieee-floating
def bigIntToFloat(bigIntlist):
	pair = []
	for bigInt in bigIntlist:
		a = format(bigInt,'x')
		while len(a)<4:
			a = "0"+a
		pair.append(bytes.fromhex(a))
		if len(pair) == 2:
			yield struct.unpack('>f', b''.join(pair))[0]
			pair = []

fields = ['time', 'pH_1', 'temp_1', 'pH_2', 'temp_2']
with open('test.csv', 'a') as f:
	writer = csv.writer(f)
	writer.writerow(fields)


### Meat of the code starts here. 




while True: 
	# connect to our modbus client
	time_current = datetime.now()

	client1 = ModbusTcpClient('192.168.1.254')
	time.sleep(2) # just to make sure thing sare good

	# These are the bytes that we want, the first 8:
	a = client1.read_input_registers(0,8).registers
	# Pull the registers off of them
	print(a)
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
	with open('test.csv', 'a') as f:
		writer = csv.writer(f)
		writer.writerow(fields)

	# close clients
	client1.close()
	time.sleep((60-time.localtime().tm_sec)%30) # run every 30 seconds
