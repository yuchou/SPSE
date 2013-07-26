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
print	'Part 2'
print

import os

"""
 
could do manip = os ... manip.getcwd()

"""

print os.getcwd() + '\n' # get current directory

directory = os.getcwd()+'/newDir' # get full path

os.rmdir(directory) # remove directory

os.mkdir("newDir") # rebuild directory


print os.listdir('.')  # list current directory content

print os.listdir('/')  # list root directory content

print os.listdir('../')  # list parent directory content

print
for item in os.listdir("."):
	if os.path.isfile(item):
		if item.count('~')==1: 
			print 'temporary file		' + item
		elif item[0]=='.':
			print 'hidden file		' + item
		else :
			print 'file			' + item
	elif os.path.isdir(item):
		print 'directory 		' + item
	elif os.path.isabs(item):
		print 'absolute 		' + item
	elif os.path.islink(item):
		print 'link 		' + item
	else:
		print 'other 			' + item

import glob
 
print
for item in glob.glob(os.path.join('.','*')):
	print item
print
for item in glob.glob(os.path.join('.','*.py')):
	print item
print
for item in glob.glob(os.path.join('.','*/')):
	print item

