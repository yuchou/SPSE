#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 4 - Part 1'
print	'Exercice'
print

"""
Download a file and monitor the progress progress using
urllib.urlrettrieve()

EDIT : wget seems a lot better

urlretrieve() takes arguments for the URL, a temporary file to hold the data, a function to report on download progress, and data to pass if the URL refers to a form where data should be POSTed. 
If no filename is given, urlretrieve() creates a temporary file. You can delete the file yourself, or treat the file as a cache and use urlcleanup() to remove it.


"""

from time import time
import urllib
import subprocess
import sys

target = 'http://www.anchorageprogramming.org/wp-content/uploads/python-logo-glassy.png'
local_file = 'file'

print '== With wget == \n' 

wget_start = time()
proc = subprocess.Popen(["wget", target])
proc.communicate()
wget_end = time()

print '== With urlretreive == \n'

def progress(nblocks, block_size, file_size) :
	print (nblocks*block_size*100)/float(file_size)

url_start = time()
urllib.urlretrieve(target, local_file, progress)
url_end = time()

print '== Results == \n'

print "wget -> %s" % (wget_end - wget_start)
print "urllib.urlretrieve -> %s"  % (url_end - url_start)

print


