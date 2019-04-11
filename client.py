#! /usr/bin/python3

import socket
import sys

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET = Address Family Internet
    # SOCK +_STREAM indicates TCP
except socket.error:
    print("failed to create socket")
    sys.exit()
    
try:    
    host = socket.gethostbyname("www.gooogle.com")
    print(host)
except socket.gaierror:
    print("failed to get host")
    sys.exit()
    
## bad from lesson, corrected below- mysock.connect(host,80)
mysock.connect((host,80))
message = "GET / HTTP/1.1\r\n\r\n"
try:
    ## mysock.sendall(message)
    mysock.sendall(message.encode())
except socket.error:
    print("failed to send")
    sys.exit()

data = mysock.recv(1000)
print(data)
mysock.close()
