#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2 - Part 6'
print	'Exercice'
print

"""
Explore multiprocessing, how does it leverage multi-core setups?
Program a TCP SYN scanner using multiprocessing.

multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.

In multiprocessing, processes are spawned by creating a Process object and then calling its start() method. Process follows the API of threading.Thread. 

The difference in implementation is that you have to provide extra protection for the __main__ thread, such that child processes don't start the subprocesses recursively. Another difference is that the Queue module is not usable for multiprocessing (maybe has to do with the fact that (child)processes do not share any memory while threads do). 
However, the multiprocessing module provides a JoinableQueue() class with the same functionality. 

"""

import sys

from multiprocessing import Process, JoinableQueue
from scapy.all import *

# # # # #

class workerProcess(Process) :

	def __init__(self, ip, queue) :
		Process.__init__(self)
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

# # #

ip = sys.argv[1]
min_port = int(sys.argv[2])
max_port = int(sys.argv[3])
portList = range(min_port, max_port+1)

# # #

queue = JoinableQueue()
for port in portList :
	queue.put(port)

# multiprocessing have extra protection for __main__ (you have to avoid that the
# child process starts each process recursively!).
if __name__=='__main__':

	for i in [1, 2, 3, 4] :
#		if not using a process object
#		worker = Process(target=WorkerProcess, args= (ip, queue))
		worker = workerProcess(ip, queue)
		worker.daemon = True
		worker.start()
		worker.join()




