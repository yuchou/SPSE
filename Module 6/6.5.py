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
print

"""
Monitoring API calls with pydbg

Steps :
Find the address of the function or API to monitor
Set a breakpoint
Dump context and inspect when a breakpoint is hit
"""

from pydbg import *
from pydbg.defines import *

# breakpoint handler
def send_bp(debugger) :
	print 'send() call'
	print debugger.dump_context(debugger.context)
	return DBG_CONTINUE

debugger = pydbg()

# list all processes and find the one we want
# debugger.enumerate_processes() => dump dict of (pid, process)
for pid, name in debugger.enumerate_processes() :
	if 'strcpy' in name :
		debugger.attach(pid)

# monitor all send calls done by the server
# find send function address 				API		func
send_api_address = debugger.func_resolve('ws2_32', 'send')
# set breakpoint on address
debugger.bp_set(send_api_address, description='send BP', handler=send_bp)

debugger.run()

# could do the same thing with revc
