#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2 - Part 3'
print	'Exercice'
print

"""
Create a multi threaded port scanner. It will take an IP range and scan it, creating threads for sub-ranges.


This does not return good answers :
def scan(port) :
	try :
		socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.connect((address, int(port)))
		socket.send('Please answer')
		socket.recv(1024)
	except :
		return False
	else :
		return True
	socket.close()
"""

import sys
from threading import Thread
from Queue import Queue, Empty
import socket
from scapy.all import sr1, IP, TCP, RandNum

# # # # #

class scannerThread(Thread) :

	def __init__(self, ip, queue) :
		Thread.__init__(self)
		self.ip = ip
		self.queue = queue

	# essential method representing the thread's activity
	def run(self) :
		while not self.queue.empty() :
			port = self.queue.get()
			# build an IP header with destination address
			ip=IP(dst=self.ip) 
			# TCP header with dest. port, SYN flag and a random sourceport > 1024
			tcp=TCP(dport=port, flags="S", sport=RandNum(1025,65535))
			resp = sr1(ip/tcp, verbose=False, timeout=0.5) # send and receive 1 packet
			if resp and resp[TCP].flags == 0x12:
				# (ACK = 0x10) + (SYN = 0x02) = (SYN-ACK = 0x12)
				print "port %s \topen" % str(port) 
			else :
				print "port %s \tclosed" % str(port) 
			self.queue.task_done()

# # # # #

ip = sys.argv[1]
min_port = int(sys.argv[2])
max_port = int(sys.argv[3])
portList = range(min_port, max_port+1)

queue = Queue()
for port in portList :
	queue.put(port)

print 'Starting scan on %s\n' %ip
for thread in range(10) :
	worker = scannerThread(ip, queue)
	worker.setDaemon(True)
	worker.start()

queue.join() # block until all tasks are done
print '\nDone'



