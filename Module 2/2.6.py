#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2'
print	'System Programming'
print	'Part 6'
print

"""
list all signals : man 7 signal  

When you type ctrl+c to send a kill signal you send a signal 7, so we will write a signal handler to change the action the signal takes.
"""

import signal
import sys

# signal handler
def ctrl_c_handler(signum, frame) :
	print "No KILLSIG allowed"
#	sys.exit(0)

print "Installing signal handler"
signal.signal(signal.SIGINT, ctrl_c_handler)

while True :
	pass
