from opcua import Client

url = 'opc.tcp://192.168.1.21:4840'
client = Client(url)
client.connect()

State = client.get_node("ns=2;i=2")
State.set_value(1)