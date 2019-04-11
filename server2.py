#! /usr/bin/python3

# week 2 raspberry pi interface
# by Chris Larson

# create socket
# bind socket to IP & port
# listen for connection
# accept connection
# receive request
# send response

import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.bind(("", 8000))
except socket.error:
    print ("failed to bind port")
    sys.exit()
    
mysock.listen(5)
while True:
    conn, addr = mysock.accept()
    data = conn.recv(1024)
    if not data:
        break
    if data:
        print("Got a request!")
    if data == b'on':
        GPIO.output(13, True)
    if data == b'off':
        GPIO.output(13, False)
    #conn.sendall(b,data)
    #print(data)
    
    conn.sendall(("HTTP/1.1 200 OK\n"
                 +"Content-Type: text/html\n"
                 +"\n"
                 +"<html><body>Hi there</body></html>").encode())
    conn.close()
    
mysock.close()
