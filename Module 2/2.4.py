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
print	'Part 4'
print

"""
CPython implementation limitation : 
Only one thread can use the interpreter at one given time
So while threads cannot be used for multiprocessing, they can still be used for I/O (for instance network reads) or for writing to disk.
"""

import thread
import time

def worker_thread(id) :
	count = 1
	print "Thread ID %d now alive." %id
	while True :
		print "Thread with ID : %d and Count : %d ; " %(id,count)
		count += 1
		time.sleep(2)

for i in range(5) :
	thread.start_new_thread(worker_thread, (i,))

print "Main thread going for a infinite loop"
while True :
	pass
