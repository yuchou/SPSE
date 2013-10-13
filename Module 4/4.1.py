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
print	'Part 1'
print

"""
fetching web pages
"""

import urllib
import pprint

#page = urllib.urlopen("http://umbo.tk")
page = urllib.urlopen("http://securitytube.net/groups?operation=view&groupId=10")

# fields
pprint.pprint(dir(page)) 
print

# response code
code =  page.code
if code == 200 :
	print 'Page successfully retreived \n'
elif code == 404 :
	print 'Page not available \n'
elif code == 405 :
	print 'Method not allowed \n'

print
print '== Headers == \n'
print page.headers

"""
gives the same content as page.headers
pprint.pprint(dir(page.headers))
print
print page.headers.items # object type
print
print page.headers.items() # object content
print

print page.headers.keys() # content of headers
for header,value in page.headers.items() :
	print header + ' : ' + value
 same as items or just headers
"""

print '== URL == \n'
base_url = "http://securitytube.net/groups"
# we need to encode arguments to be abble to use them easilly
args = { 'operation' : 'view', 'groupId' : 10 }
# works well : 
#	args = { 'operation' : 'view all', 'groupId' : 10 }
encode_args = urllib.urlencode(args)
print encode_args

fp2 = urllib.urlopen(base_url + '?' + encode_args) # GET
fp2 = urllib.urlopen(base_url, encode_args) # POST
#print fp2.read()
print fp2.code


#print 'HTML content \n'
#print page.read() 
