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
print	'Part 5'
print


"""
Create task queues
Threads receive tasks
Threads complete tasks and inform the queue
All threads exit once queue is emptuy

http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/

"""

import threading
import Queue
import time

class workerThread(threading.Thread) : # subclass of threading.Thread

	# must be included if using more then the self paratemer
	def __init__(self, queue) : # queue from where we will get tasks/jobs
		threading.Thread.__init__(self) # calls parent
		self.queue = queue # assign it to the internal queue variable

	# essential method representing the thread's activity
	def run(self) :
		print "In worker thread ; "
		while True :
			counter = self.queue.get() # get next task in queue
			print "Ordered to sleep for %d seconds ; " %counter
			time.sleep(counter)
			print "Finished sleeping for %d seconds ; " %counter
			self.queue.task_done() # set task as completed

queue = Queue.Queue() # get a queue to use 

for j in range(10) :
	queue.put(j) # put numbers 0-9 inside queue

for i in range(5) :
	print "Creating workerThread : %d ; " %i
	worker = workerThread(queue)
	worker.setDaemon(True) # or else task will not exit upon completion
	worker.start()
	print "workerThread %d created ; " %i

queue.join() # wait for task queue to be empty
# once task queue is empty exit   
print "Task over."
