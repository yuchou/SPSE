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

"""
PF_Packet interface to capture raw packets

# packing in Little endian
struct.pack('B', 1)  # byte
struct.pack('H', 1)  # unsigned short int
struct.pack('L', 1)  # unsigned long int

# packing in Big endian
struct.pack('>B', 1)  # byte
struct.pack('>H', 1)  # unsigned short int

# for internet need to send content in Big endian format
struct.pack('!L', 1)  # unsigned long int

# unpack long int
struct.pack('!L', '\x00\x00\x00\x01') 

"""

import socket
import struct
import binascii

# put the interface on promiscuous mode
# -> ifconfig eth0 promisc


# packet interface & raw sockets & protocol to filter 0x0800==IP protocol
# check protoocols in /usr/include/linux/if_ether.h
raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

print '\n[+] Packet'
packet = raw_socket.recvfrom(2048)
print packet

print '\n[+] Ethernet header'
ethernetHeader = packet[0][0:14]
(src_mac, dst_mac, ethertype) = struct.unpack('!6s6s2s', ethernetHeader)
print binascii.hexlify(src_mac)
print binascii.hexlify(dst_mac)
print binascii.hexlify(ethertype)

print '\n[+] IP header'
ipHeader = packet[0][14:34]
(wtv, src_ip, dst_ip) = struct.unpack('!12s4s4s', ipHeader)
print binascii.hexlify(wtv)
print binascii.hexlify(src_ip)
print binascii.hexlify(dst_ip)

print '\n[+] TCP header'
tcpHeader = packet[0][34:54]
(src_port, dst_port, wtv) = struct.unpack('!HH16s', tcpHeader)
print binascii.hexlify(str(src_port))
print binascii.hexlify(str(dst_port))
print binascii.hexlify(wtv)

# ntoa prints the hex values into IP syntax
print '\nSource IP address \t\t %s:%s' %(socket.inet_ntoa(src_ip), src_port)
print 'Destination IP address \t\t %s:%s' %(socket.inet_ntoa(dst_ip), dst_port)



