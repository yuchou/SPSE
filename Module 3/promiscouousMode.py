#!/usr/bin/env python

import struct
import fcntl
import socket
import sys

IFF_PROMISC = 0x100
SIOCGIFFLAGS = 0x8913
SIOCSIFFLAGS = 0x8914

def changePromiscMode(iface = 'eth0', toPromisc = True):
	l = len(iface)

	rsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	ifreq = struct.pack('%ss%sxH'%(l,16-l),iface,0)
	ifreq =	fcntl.ioctl(rsock.fileno(), SIOCGIFFLAGS,ifreq)
	(flags,) = struct.unpack('16xH',ifreq[:18])
	
	if toPromisc == (flags & IFF_PROMISC > 0):
		return
	
	if toPromisc:
		flags = flags | IFF_PROMISC
	else:
		flags = flags & ~IFF_PROMISC

	ifreq = struct.pack('%ss%sxH'%(l,16-l), iface, flags)
	fcntl.ioctl(rsock.fileno(), SIOCSIFFLAGS, ifreq)

usageNotes = """
Usage:
------
type in promiscouousMode.py [iface] -promisc to enable promiscouous mode

\t\tor

type in promiscouousMode.py [iface] to disable promiscouous mode
		
"""

args = sys.argv
validIfaces = ['eth0']
del args[0]
if len(args) == 1:
	if args[0] in validIfaces:
		changePromiscMode(args[0], False)
	else:
		print usageNotes
elif len(args) == 2:
	if args[1] == '-promisc' and args[0] in validIfaces:
		changePromiscMode(args[0],True)
	else:
		print usageNotes
else:
	print usageNotes