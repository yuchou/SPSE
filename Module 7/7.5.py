#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 7'
print	'Part 1'
print

"""
nmap automation in python

xael.org/norman/python/python-nmap/
"""

import nmap
import sys

host = sys.argv[1]
port = sys.argv[2]

# scanner object
nmScan = nmap.PortScanner()

def scan(host, port) :
	nmScan.scan(host, port) # the object is a dict 
	state = nmScan[host]['tcp'][int(port)]['state']
	#print nmScan[host]['tcp'][int(port)]
	print '[*] ' + host + ' tcp/' + port + ' ' + state

ports = port.split(',')
for target_port in ports :
	scan(host, target_port)

