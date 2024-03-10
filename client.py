#!/usr/bin/env python3

from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient('localhost', port=5020)

while not client.connected:
    client.connect()
    time.sleep(1)

client.write_coil(1, True)
client.write_register(1,True)
result = client.read_coils(1,1)
print(result.bits[0])
result = client.read_holding_registers(1,1)
print(result.registers[0])
client.close()
