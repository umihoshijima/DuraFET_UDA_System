from pymodbus.client.sync import ModbusTcpClient
import struct # used for the hex stuff
import time  # used to pause script
# https://github.com/riptideio/pymodbus

client1 = ModbusTcpClient('192.168.1.254')
time.sleep(1)

# Much thanks to Stack Overflow commenter Nathan for this: 
https://stackoverflow.com/questions/48217264/python-converting-two-sequential-2-byte-registers-4-bytes-into-ieee-floating
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
temp_1 = next(dat)
temp_2 = next(dat)

pH_1 = next(dat)
pH_2 = next(dat)

# Used this doc here: https://docs.python.org/3.5/tutorial/inputoutput.html

print( 'Probe 1: pH of {0:.3f} and temperature of {1:.3f} C'.format(pH_1, temp_1))
print( 'Probe 2: pH of {0:.3f} and temperature of {1:.3f} C'.format(pH_2, temp_2))

client.close()
