from MeasurementReader import *
import requests
from datetime import datetime
from ConfigReader import base_url


baseurl = base_url
lastTemp = 172
lastHum = 0

def log_data(logText):
    with open("log.txt", "a") as f:
        f.write(str(datetime.now()) + " - " + logText + "\n")
        
def send_data(temperature, humidity):
    now = datetime.now()
    date = now.strftime("%Y-%m-%dT%H:%M:%S")
    json = {"partitionKey":"default","dateTime":date, "temperature":float(temperature),"humidity":float(humidity)}
    r = requests.post(url= baseurl + "/values", json = json)
    log_data("Status code: " + str(r.status_code))
    
def tempHasChanged(temperature):
    diff = lastTemp - temperature
    if diff >= 0.5 or diff <= -0.5:
        return True
    else:
        return False

print("Seansor app started")

while True:
    try:
        temp, hum = return_values()
        #print("Temp: new{} - last {}".format(temp, lastTemp))
        #print("Hum: new {} - last: {}".format(hum, lastHum))       
        if tempHasChanged(temp):
            lastTemp = temp
            lastHum = hum
            send_data(temp, hum)
        #else:
        #    print("No changes")
    except RuntimeError as error:
        #print(error.args[0])
        log_data("Error: " + str(error.args[0]))
        continue
    except Exception as error:
        sensor.exit()
        continue
    time.sleep(10)   