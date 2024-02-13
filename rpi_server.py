from opcua import Server
import time
import RPi.GPIO as GPIO

server = Server()
url = 'opc.tcp://192.168.1.21:4840'
server.set_endpoint(url)

name = "OPCUA_RASPBERRYPI_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()
Param = node.add_object(addspace, "Parameters")

#When server starts, this variable is set to 10
#From a client app, we can change this value, the idea:
# 1 = ON
# 0 = OFF
State = Param.add_variable(addspace, "State", 10)
State.set_writable()

server.start()
print(f"Server started at {url}")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    #Will be waiting for changes from client app
    xState = State.get_value()
    print(xState)

    # See the led in rpi
    if xState == 1:
        GPIO.output(18, GPIO.HIGH)
        print("LED is ON")
    
    elif xState == 0:
        GPIO.output(18, GPIO.HIGH)
        print("LED is OFF")

    time.sleep(2)