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
Explore other modules available for automation of an ssh login process

=> don't forget the ''
"""

import pxssh
import sys

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

def send_command(session, command) :
	session.sendline(command)
	session.prompt()
	print session.before

def connect(host, user, passowrd) :
	try :
		session = pxssh.pxssh()
		session.login(host, user, password)
		return session
	except :
		print '[-] Error connecting'
		exit(0)

session = connect(host, user, password)
send_command(session, command)
