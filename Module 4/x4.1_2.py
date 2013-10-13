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
urlencode() does a bad job in handling special characters in the url
une .quote() and .quote_plus() and illustrate how they can help
"""

import urllib

# # #

print '== urlencode == \n'

args = { 'operation' : 'view', 'groupId' : 10 }

encoded_args = urllib.urlencode(args)

print encoded_args + '\n'


args = { 'operation' : 'view', 'groupId' : 'is~some text' }

encoded_args = urllib.urlencode(args)

print encoded_args + '\n'

# # #

print '== quote == \n'

args = "this&is~some text"

encoded_args = urllib.quote(str(args))

print encoded_args + '\n'

# # #

print '== quote_plus == \n'

encoded_args = urllib.quote_plus(str(args))

print encoded_args + '\n'
