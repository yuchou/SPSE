#!/usr/bin/python
# -*- coding: utf-8 -*-

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
print

"""
Create a wifi sniffer and print out the unique SSIDs of the wifi networks in your vincinity

http://hackoftheday.securitytube.net/2013/03/wi-fi-sniffer-in-10-lines-of-python.html

http://www.cs.wright.edu/~pmateti/InternetSecurity/Lectures/WirelessHacks/Mateti-WirelessHacks.htm
http://www.packetstan.com/2011/03/extracting-ap-names-from-packet.html
"""

from scapy.all import *
import sys

interface = str(sys.argv[1])

ap_dict = {}

def ssid_sniffer(packet) :
	# check if 802.11 packet
	if packet.haslayer(Dot11) :
		# check if management frame and beacon frame
		if packet.type==0 and packet.subtype==8 :
			# addr2 and addr3 -> MAC
			if packet.addr2 not in ap_dict.keys() :
				# info -> SSID	
				# add new AP to dict
				ap_dict[packet.addr2] = packet.info
				# print new AP information
				print '| %s |\t %s' %(packet.addr2, packet.info.strip('\n'))

print '|--------MAC--------|------SSID------|'
while True :
	try :
		sniff(iface=interface, count=1, prn=ssid_sniffer)
	except Exception, txt :
		pass
