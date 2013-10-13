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
print	'Part 2'
print

"""
parsing data, need to
	=> receive and parse 			<= this part
	=> generate and send request for data 	<= part 1

"""

import urllib
from bs4 import BeautifulSoup

url ="http://securitytube.net/video/3000"
html = urllib.urlopen(url)

#print html
#print html.code

page = BeautifulSoup(html.read(), "lxml") # force BS to use LXML instead of htmlparser

print page.title # prints according to html tag objects
print page.title.string # navigable string
print page.title.name # tag
print

# bad way
#print page.meta
#print page.meta.next
#print page.meta.next.next

allMetaTags = page.find_all('meta') # all meta tags
# very powerful, can even take regexp

#print allMetaTags
print 1
for element in allMetaTags :
	print element
print
print 2
for element in allMetaTags :
	print element['content']
print

print 3L
# find all the links in the page
links = page.find_all('a') # a tags before hrefs
print len(links)
print links[3]
print links[3].string
print links[3]['href']
print

'''
for link in links :
	print link.string
	print link['href']
	print
# '#' represents an exact position in the current document, an anchor
'''

# extract all text
#print page.get_text() # good for data mining


