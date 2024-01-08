# Modbus Client
from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.payload import BinaryPayloadBuilder
import time

print("Start Modbus Client")
# initialize a modbus TCP Client
client = ModbusClient(host="127.0.0.1", port=502)
reg = 0
address = 0

# initialize data
data = [10, 11, 12, 13, 14]

for i in range(10):
    print("-" * 5, "Cycle ", i + 1, "-" * 5)
    time.sleep(0.5)

    # increment data by one
    for i, d in enumerate(data):
        data[i] = d + 1

    # time.sleep(0.5)
    # write holding registers (40010 to 40015)
    print("Write", data)
    time.sleep(0.5)

    # binary representation of the data stored in the data list
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    # Binary Payload Builder is used to construct binary payloads for Modbus communication

    for d in data:
        builder.add_16bit_int(int(d))
    payload = builder.build()
    result = client.write_registers(
        int(reg), payload, skip_encode=True, unit=int(address)
    )

    # read holding registers
    rd = client.read_holding_registers(reg, len(data)).registers
    print("Read", rd)
    time.sleep(0.5)

client.close()
