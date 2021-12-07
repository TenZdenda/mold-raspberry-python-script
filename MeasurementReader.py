import socket

from sense_hat import SenseHat
sensehat = SenseHat()

def return_values ():
        try:
            temp = round(sensehat.get_temperature())
            hum = round(sensehat.get_humidity()) 
            return temp, hum       
        except RuntimeError as error:
            #print(error.args[0])
            #raise error
            pass
        except Exception as error:
            sensehat.exit()
            raise error

response = return_values()