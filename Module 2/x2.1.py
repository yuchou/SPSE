#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2'
print	'Part 1'
print	'Exercice'
print

'''
read /var/log/messages
find all logs pertaining to a usb and print them

'''


logfile = '/var/log/messages'

log = open(logfile, 'r').readlines()

for line in log :
	if '] usb ' in line.lower() :
		print line
