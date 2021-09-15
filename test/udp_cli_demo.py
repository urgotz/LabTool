import socket

 

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ('192.168.1.30', 8089)
# serverAddressPort   = ('127.0.0.1', 8089)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send to server using created UDP socket

print( UDPClientSocket.sendto(bytesToSend, serverAddressPort) )

 

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print(msgFromServer)
 

msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
