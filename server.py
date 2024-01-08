# modbus server (TCP Transmission Control Protocol)

from pymodbus.server import StartTcpServer # starts the server
from pymodbus.datastore import ModbusSequentialDataBlock # define data blocks (discrete inputs, coils, holding and input registers)
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext # create a context for server to manage data and handle requests

def run_async_server():
    nreg = 200 # number of registers to be initialized

    # initialize data store
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [15]*nreg),
        co=ModbusSequentialDataBlock(0, [16]*nreg),
        hr=ModbusSequentialDataBlock(0, [17]*nreg),
        ir=ModbusSequentialDataBlock(0, [18]*nreg)
    )
    # context, which is the server context that includes the data store initialized in the previous step 	
    context = ModbusServerContext(slaves=store, single=True)

    # TCP Server 
    StartTcpServer(context=context, host='localhost',\
                   address=(
                       "127.0.0.1",502)
                       )

if __name__ == "__main__":
    print('Modbus server started on localhost port 502')
    run_async_server()