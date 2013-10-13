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
print	'Part 8'
print

"""
Programming with Scapy


"""

from scapy.all import *

# find fields of arp request
# ls(ARP)

# ARP scanner for the entire subnet
for lsb in range(1,256) :
	ip = '192.168.0.'+str(lsb)
	# ff... all broadcast packet	
	arpRequest = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip, hwdst='ff:ff:ff:ff:ff:ff')
	# send it out, waiting for a response
	arpResponse = srp1(arpRequest, timeout=1, verbose=0)
	if arpResponse :
		print 'IP: '+ arpResponse.psrc + ' MAC: ' + arpResponse.hwsrc



