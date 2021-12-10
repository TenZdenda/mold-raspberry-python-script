from datetime import datetime
from sense_hat import SenseHat
from time import sleep
import socket
import json

sensehat = SenseHat()

lastTemp = 172
lastHum = 0

serverIPAddress = "255.255.255.255"
serverPort = 10100

def return_values ():
        try:
            temp = round(sensehat.get_temperature())
            hum = round(sensehat.get_humidity()) 
            return temp, hum 
        except RuntimeError as error:
            pass
        except Exception as error:
            sensehat.exit()
            raise error

def send_data(temperature, humidity):
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    jsonObject = {"Id":int(1), "Temperature":int(temperature),"Humidity":int(humidity),"Device": "Default","CreatedAt": date}
    jsonString = json.dumps(jsonObject)

    # Create a client side UDP socket
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #was DGRAM

    # Manually enable the broadcast
    UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(jsonString.encode(), (serverIPAddress, serverPort))
    
    #just a test for if there is any return
    #print(jsonString.encode())

def tempHasChanged(temperature):
    diff = lastTemp - temperature
    if diff >= 0.5 or diff <= -0.5:
        return True
    else:
        return False

print("Seansor app activated")

while True:
    try:
        temp, hum = return_values()  
        if tempHasChanged(temp):
            lastTemp = temp
            lastHum = hum
            send_data(temp, hum)
            #print('Hello')
    except RuntimeError as error:
        send_data("Error: " + str(error.args[0]))
        continue
    except Exception as error:
        sensehat.exit()
        continue
    sleep(10)
