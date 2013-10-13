#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 4'
print	'Attacking Web Applications'
print	'Part 6'
print

"""
XML parsing and web services


"""

from bs4 import BeautifulSoup
import pprint


xml = open('defcon.rss', 'r').read()

bs = BeautifulSoup(xml, 'xml') # xml instead of lxml

#pprint.pprint(dir(bs))

for item in bs.find_all('item') :
	print item.title.string
	print item.link.string
	print
