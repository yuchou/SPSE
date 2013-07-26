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
Use a locks to create threads that share resources

http://linuxgazette.net/107/pai.html

Now that we have one thread running, running multiple threads is as simple as calling start_new_thread() multiple times. The problem now would be to synchronize the many threads which we would be running. Synchronization is done using a Lock object. Locks are created using the allocate_lock() factory function.

Locks are used as mutex objects, and are used for handling critical sections of code. A thread enters the critical section by calling the acquire() method, which can either be blocking or non-blocking. A thread exits the critical section, by calling the release() method.

"""

import time
import thread
import threading
import Queue

class workerThread(threading.Thread) : # subclass of threading.Thread

	# must be included
	def __init__(self, queue) : # queue from where we will get tasks/jobs
		threading.Thread.__init__(self) # calls parent
		self.queue = queue # assign it to the internal queue variable

	# essential ethod representing the thread's activity
	def run(self) :
		print "In worker thread ; "
		while True :
			lock.acquire()
			counter = self.queue.get()
			print "Ordered to sleep for %d seconds ; " %counter
			time.sleep(counter)
			print "Finished sleeping for %d seconds ; " %counter
			self.queue.task_done()
			lock.release()

"""
The difference is you see the times are really divided as, even though we are using threads, only one can run at a given time as the body of the thread is always on a lock
"""

queue = Queue.Queue() # get a queue to use 
lock = thread.allocate_lock()

for i in range(10) :
	print "Creating workerThread : %d ; " %i
	worker = workerThread(queue)
	worker.setDaemon(True) # or else task will not exit upon completion
	worker.start()
	print "workerThread %d created ; " %i

for j in range(10) :
	queue.put(j) # put numbers 0-9 inside queue

queue.join() # wait for task queue to be empty

# once task queue is empty exit   
print "Task over."




