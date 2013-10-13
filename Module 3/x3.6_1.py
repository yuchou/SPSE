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
Create a packet sniffer for the HTTP prococol and print the HTTP headers and data in get/posts

HTTP : http://www.networksorcery.com/enp/protocol/http.htm_

1 = GET
2 = POST
3 = GET and POST
4 = HTTP content
5 = GET & POST & HTTP content
"""

from scapy.all import *
import re
import sys

interface = str(sys.argv[1])
content = int(sys.argv[2])

def filterHTTP(packet):
	if packet.haslayer(Raw):
		packet_load = str(packet["Raw"])
		header = packet_load.split("\r\n")

		should_print = False
		if re.match("GET.", header[0]) and (content==1 or content==3 or content==5) :
			should_print = True
		elif re.match("POST.", header[0]) and (content==2 or content==3 or content==5) :
			should_print = True
		elif re.match("HTTP.", header[0]) and (content==4 or content==5) :
			should_print = True
		if should_print :
			if content==4 :
				#print header[-1]
				print packet['Raw']
				return
			print packet.summary()
			print
			for line in header :
				print str(line) 
  			print "* * * * * * * * * * * * * * * * * * *"

if __name__=="__main__":
	sniff(iface=interface, prn=filterHTTP)
