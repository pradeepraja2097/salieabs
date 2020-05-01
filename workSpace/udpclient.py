import socket
 
UDP_IP = "192.168.43.172"
UDP_PORT = 5683
MESSAGE = b'hello'
 
print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

 
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
print ("message:", MESSAGE)

