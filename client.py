from opcua import Client
import time

url = 'opc.tcp://192.168.1.16:4840'
client = Client(url)
client.connect()
print(f"Client connected to {url}")

while True:
    #Get nodes!
    Temp = client.get_node("ns=2;i=2")
    Press = client.get_node("ns=2;i=3")
    Time = client.get_node("ns=2;i=4")
    
    #Print just values
    print(Time.get_value(), Temp.get_value(), Press.get_value())
    time.sleep(2)