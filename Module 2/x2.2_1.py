#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2'
print	'Exercice 1'
print

"""
Takes a path and a file type and prints recursively all files of the selected file type contained in the folders.
"""

import sys
import os 
import glob

path = str(sys.argv[1])
filetype = str(sys.argv[2])
searchDepth = 1

def getTabString(depth) :
	tabString = ''
	for i in range(depth-1):
		tabString = str(tabString+'----')
	return tabString

def recursiveFInd(path, filetype, depth) :
	print getTabString(depth) + path
	for item in glob.glob(os.path.join(path,str('*.'+filetype))):
		fileName = item.split('/')[-1]
		print getTabString(depth) + fileName
	for item in glob.glob(os.path.join(path,'*/')):
		depth = depth + 1
		recursiveFInd(item, filetype, depth)

recursiveFInd(path, filetype, searchDepth)
print
