from opcua import Server
from random import randint
import datetime, time

server = Server()
url = 'opc.tcp://192.168.1.16:4840'
server.set_endpoint(url)

name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")

Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
Time = Param.add_variable(addspace, "Time", 0)
Temp.set_writable()
Press.set_writable()
Time.set_writable()

server.start()
print(f"Server started at {url}")

while True:
    xTemp = randint(10, 50)
    xPress = randint(200, 999)
    xTime = datetime.datetime.now()

    Temp.set_value(xTemp)
    Press.set_value(xPress)
    Time.set_value(xTime)
    
    print(xTime, "Temp:", xTemp, "Press:", xPress)
    time.sleep(2)