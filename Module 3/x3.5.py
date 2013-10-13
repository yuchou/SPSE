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
print	'Part 4'
print

"""
Send an ARP request packet using raw sockets.

Check packet content :
tcpdump -i eth0 arp

http://www.networksorcery.com/enp/protocol/arp.htm
http://www.technicalhowto.com/protocols/arp/arp.html 

"""

import socket
import struct

raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))

raw_socket.bind(('eth0', socket.htons(0x0806)))

source_ip = socket.inet_aton("192.168.0.100")
destination_ip = socket.inet_aton("127.0.0.0")
source_mac = '\x50\xe5\x49\xd7\xff\xfd' 
destination_mac = '\x00\x00\x00\x00\x00\x00' 

ethernetHeader = struct.pack("!6s6s2s", destination_mac, source_mac, '\x08\x06')
arpHeader = struct.pack("!2s2s1s1s2s", '\x00\x01', '\x08\x00', '\x06', '\x04', '\x00\x01')
arp_source = struct.pack("!6s4s", source_mac, source_ip)
arp_destination = struct.pack("!6s4s", destination_mac, destination_ip)

arp_packet = ''.join([ethernetHeader, arpHeader, arp_source, arp_destination])
raw_socket.send(arp_packet) 

