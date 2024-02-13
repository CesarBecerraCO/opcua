from opcua import Client
import time

url = 'opc.tcp://VPROSYS:53530/OPCUA/SimulationServer'
client = Client(url)
client.connect()
print(f"Client connected to {url}")

while True:
    #Get nodes!
    p = client.get_node("ns=3;i=Active.Power")
    
    #Print just values
    print(p.get_value())
    time.sleep(1)