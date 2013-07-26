#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2'
print	'Exercice 2'
print

"""
Takes a path and prints information about all the files it contains

could also use os.stat(file)
"""

import sys
import os 
import glob

path = str(sys.argv[1])

for item in os.listdir(path) :
	if item.count('~')==1: 		# temporary file
		continue
	elif item[0]=='.': 		# hidden file
		continue
	elif os.path.isdir(item)| os.path.isfile(item) | os.path.isabs(item):	# files and directories	
		print os.path.abspath(item)
		print os.path.basename(item)
#		print os.path.exists(item)
		print os.path.getatime(item)
		print os.path.getmtime(item)
		print os.path.getctime(item)
		print os.path.getsize(item)
		print os.path.isabs(item)
		print os.path.isfile(item)
		print os.path.isdir(item)
		print os.path.islink(item)
		print os.path.ismount(item)
		print os.path.normpath(item)
		print os.path.realpath(item)
		print


