#!/usr/bin/python

"""
Client that will connect to the server.
Created exactly like the server but with client-side sockets

"""

import sys
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# give ip/port to connect to as argument
client_socket.connect((sys.argv[1], int(sys.argv[2])))

while True :
	userInput = raw_input("Please enter a string : ")
	client_socket.send(userInput)
	print client_socket.recv(2048)

client_socket.close()
