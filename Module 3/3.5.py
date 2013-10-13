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
print	'Part 5'
print

"""
If we can send random packets in the network then we can send anything we want

Run as root

view packet content :
sudo tcpdump -i eth0 -vv -XX "not port 22"

"""

import socket
import struct

# packet interface & raw sockets & protocol to filter 0x0800==IP 
raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

# bind socket to interface & protocol for injection 
raw_socket.bind(('eth0', socket.htons(0x0800)))

# packet content -> destination mac address & source mac address & ethertype==IP
# ethernet header, len=14
packet = struct.pack('!6s6s2s', '\xaa\xaa\xaa\xaa\xaa\xaa', '\xbb\xbb\xbb\xbb\xbb\xbb', '\x08\x00')

# sent packet with random string
raw_socket.send(packet + 'randomContent')
