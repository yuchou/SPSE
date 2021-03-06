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
Create a list of FTP sites
Create a workerThread and queue which can login to these sites and list root directory and exit
Use 5 threads for this job and 10 FTP sites
"""
import Queue
import threading
from ftplib import FTP

ftpList = ['ftp.aao.gov.au', 
			'ftp.al.com.au', 
			'ftp.jcu.edu.au',
			'ftp.marine.csiro.au',
			"ftp.cs.brown.edu",
			"ftp.3k.com",
			"ftp.aero.jussieu.fr",
			"ftp.linux.hr",
			"ftp.invircible.co.il",
			"ftp.avm.de"]

# # #

class WorkingThread(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while not self.queue.empty() :
			ftp = self.queue.get()
			ftp_access(ftp)
			self.queue.task_done()


def ftp_access(ftp) :
	try :
		url = FTP(ftp)
		url.login()
	except :
		print 'Unable to log into %s' %ftp
	else :
		lock.acquire()
		print "-"*10,ftp,"-"*10
		print url.retrlines('LIST')
		print"\n"
		url.quit()
		lock.release()


# # #

queue = Queue.Queue()
lock = threading.Lock()

for ftp in ftpList:
	queue.put(ftp)

for i in ftpList:
	worker = WorkingThread(queue)
	worker.setDaemon(True)
	worker.start()

queue.join()
print 'Done'
