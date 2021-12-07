import socket
import time

messageFromClient = "Connected"
bytesToSend = str.encode(messageFromClient)
serverIPAddress   = "http://localhost:23864/api/MoldProjectAPI"
serverPort = 10100
bufferSize = 1024

# Create a UDP socket at the client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Manually enable the broadcast
UDPClientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, (serverIPAddress, serverPort))
