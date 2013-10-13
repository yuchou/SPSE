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
print	'Exercice'
print '\n-------------------------------------------------------------------\n'

'''
Find how to put the interface in promiscuous mode from inside the code
=> not so easy / useful

Write a TCP packet sniffer that can parse a full packet and print all the fields.
Enable the parser to make some filtering

Create a sniffer only for HTTP packets (TCP, port 80)

tcp options
http://stackoverflow.com/questions/6639799/calculate-size-and-start-of-tcp-packet-data-excluding-header

detailed answer :
https://bitbucket.org/chbb/spse/src/master/module3/RawSocketSnifferHTTP.py?at=master

huge answer :
http://student.securitytube.net/mod/forum/discuss.php?d=738

explains fields well :
http://student.securitytube.net/mod/forum/discuss.php?d=678

'''
import socket
import struct
import binascii

# put the interface on promiscuous mode
# -> ifconfig eth0 promisc

def format_MAC(MAC_address) :
	return MAC_address[0:2]+':'+MAC_address[2:4]+':'+MAC_address[4:6]+':'+MAC_address[6:8]+':'+MAC_address[8:10]+':'+MAC_address[10:12]

raw_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

while True : # not isHTTP :

	packet = raw_socket.recvfrom(2048) # wait for packet to arrive

	# Ethernet/frame header
	# the preamble (8 bit) is ripped off
	ethernet_header = packet[0][0:14]
	(sourceMAC, destinationMAC, ethertype) = struct.unpack('!6s6s2s', ethernet_header)
	
	# IP header
	ip_header = packet[0][14:34]
	(data, sourceIP, destinationIP) = struct.unpack('!12s4s4s', ip_header)
	
	# TCP header
	tcp_header = packet[0][34:54]
	(source_port, destination_port, data) = struct.unpack('!HH16s', tcp_header)

	if source_port == 80 or destination_port == 80 :
		print 'destination MAC :\t', format_MAC(binascii.hexlify(destinationMAC))
		print 'source MAC :\t\t', format_MAC(binascii.hexlify(sourceMAC))
		print 'destination IP :\t', socket.inet_ntoa(destinationIP)
		print 'source IP :\t\t', socket.inet_ntoa(sourceIP)
		print 'destination port :\t', destination_port
		print 'source port :\t\t', source_port
		print

		# unidentified 12 bytes at the beginning
		print packet[0][66:len(packet[0])]
		print
		print binascii.hexlify(packet[0][66:len(packet[0])])
		print '-------------------------------------------------------------------\n'
