#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 3'
print	'Network Security'
print	'Part 1'
print

import socket # API : http://docs.python.org/2/library/socket.html

"""
This is an echo server, it can connect to clients to receive strings and send them back
"""

# SETUP PROTOCOL & PORT & SOCKET

"""
address family, tipically AF_INET for internet applications
kind of socket required, from a reliability perspective. in this case, because we use tcp, SOCK_STREAM
for UDP, use datagram sockets
"""
socket_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

"""
assure that if the server disconnects, the address is again available quickly
"""
socket_TCP.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""
bind socket to a port and interface on the interface's network stack
IP associated to the interface on which the socket should listen on, and the port number on that ip address. has to be passed as a tuple
"""
socket_TCP.bind(("0.0.0.0", 8000)) 

# WAIT FOR CONNECTION TO A CLIENT

"""
start inviting connections by listening on that IP address+port for clients
number of concurrent clients the socket can handle
"""
socket_TCP.listen(2) 

print "Waiting for clients ; "
"""
each new client has a socket that is assigned to him
whill wait till a client connects
	=>	connect with : nc ipaddress 8000 
"""
(client, (ip, port)) = socket_TCP.accept()

print "Received connection from : %s ; " %ip # ip of the connected client

# SEND AND RECEIVE DATA TO AND FROM CLIENT

print "Starting ECHO output ; "
client.send("START ECHO \n")

data = 'dummy'

while len(data) : # keep echo while not zero
	data = client.recv(2048) # receive 2048 bytes from client
	print "Client sent : %s " %data
	data = "You sent : "+data
	client.send(data)

print "Closing connection."
client.close()

print "Shutting down server."
