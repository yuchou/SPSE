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
print	'Part 3'
print

import os

"""
Fork
Basically the program is separated into two executions. The firs one with a non-zero childPID value (the parent) and the other with a childPID=0. 
We use this value to have the processes run different code.
The binaries of parent and child are the exact same.

"""

def print_child_process() :
	print "Child process pid : %d" %os.getpid()
	print "Child is exiting"	
	# os.fork() would return 0

def parent_process() :
	print "Parent process pid : %d" %os.getpid()
	childPID = os.fork() # create new process, returns PID of child

	if childPID == 0 : 
		# we are inside child
		print_child_process()
	else :
		# we are inside the parent
		print "We are inside the parent"
		print "The child PID is %d" %childPID

parent_process()
print

"""
Exec
Overlays the parent with a new process with totally different binaries.
The parent process no longer remains, the child process overlays completey
"""

import os

os.execvp("ping", ["ping", "google.ca"]) # will overlay the current process and exit the python interpretter and the ping program will run with argument [...]
# note that usually you would have to give the full path

# when you kill the ping program we do not return to the parent
print "I'm back!"










