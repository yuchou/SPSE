#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 6'
print	'Exercice'
print

"""
Take an executable as input and run it automatically => find pid

Also include full crash dump details (registers, stack, etc) => get info with utils module

https://github.com/OpenRCE/sulley/wiki/Windows-Installation
http://wikisecure.net/security/pydbg-an-installation-guide

"""

#-----------------------#
# Imports				#
#-----------------------#

from pydbg import *
from pydbg.defines import *
import utils

import sys
import subprocess

#-----------------------#
# Variables				#
#-----------------------#

default_path = "C:\\Documents and Settings\\Administrator\\"
#user_path = sys.argv[1]
user_path = 'Desktop/strcpy_server'
path = default_path + user_path.replace('/', '\\')

#-----------------------#
# Functions				#
#-----------------------#

def detect_overflow(dbg) :
	if dbg.dbg.u.Exception.dwFirstChance : # ignore first chance exceptions
		return DBG_EXCEPTION_NOT_HANDLED
	#print '\n==ACESSVIOLATION=='
	#print 'ESP \t\t %0X' %dbg.context.Esp
	#print 'EIP \t\t %0X' %dbg.context.Eip
	
	print dbg.dump_context()

	return DBG_EXCEPTION_NOT_HANDLED # ensure that we return

#-----------------------#
# Main					#
#-----------------------#

print 'Starting \t %s' %path
process = subprocess.Popen(path)

pid = process.pid
print 'Process PID \t %s' %str(pid)

# create debugger object
dbg = pydbg()

# attach to a running process using its pid
dbg.attach(pid)

# access violation exception + handler (user defined function)
dbg.set_callback(EXCEPTION_ACCESS_VIOLATION, detect_overflow)
dbg.run() # keep running program despite exception


