#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 6'
print	'REverse Engineering'
print	'Part 4'
print

"""
Install pydbg on Windows :
https://github.com/OpenRCE/sulley/wiki/Windows-Installation
http://wikisecure.net/security/pydbg-an-installation-guide
http://www.glamenv-septzen.net/en/view/13

pydbg
http://code.google.com/p/paimei/

info
http://www.securityxploded.com/api-call-tracing-with-pefile-pydbg-and-idapython.php

We are not interested in first chance exceptions as they don't necessarily mean anything.

Could just constantly check the value of eip to look for eip=41414141 to find possible buffer overflows, and if found check the values and offsets on the stack.
"""

from pydbg import *
from pydbg.defines import *

import sys

def detect_overflow(dbg) :
	if dbg.dbg.u.Exception.dwFirstChance : # ignore first chance exceptions
		return DBG_EXCEPTION_NOT_HANDLED
	print 'Access violation EIP : %0X' %dbg.context.Eip
	return DBG_EXCEPTION_NOT_HANDLED # ensure that we return

# create debugger object
dbg = pydbg()

# attach to a running process using its pid
dbg.attach(int(sys.argv[1]))

# access violation exception + handler (user defined function)
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, detect_overflow)
dbg.run() # keep running program despite exception
