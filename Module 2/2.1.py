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
print	'Part 1'
print

"""
w : 	write, if it doesn't exist it creates it, if it exists it overwrittes it
a : 	append, if it doesn't exist it creates it, if it exists it opens it
	The content added is at the end of the existing data
r:	read

http://www.peterbe.com/plog/blogitem-040312-1

"""

"""

fileContent = open("sometextfile", "a") 

print fileContent

for count in range(100):
	fileContent.write(str(count) )#+ "\n")

fileContent.close()

"""

fileContent = open("sometextfile", "r") 

#for line in fileContent.readlines():
#	print line.strip() # skips the newline added by the print

print fileContent.readline()
print fileContent.readline()

print fileContent.xreadlines()

#for line in fileContent.readline():
#	print line.strip() # skips the newline added by the print

fileContent .close()

### playing with files

import os

# os.rename('nameA.txt','nameB.txt')
# os.delete('name.txt')
