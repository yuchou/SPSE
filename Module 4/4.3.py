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
print	'Part 3'
print

"""
Coding a screen scaper

"""

import urllib
from bs4 import BeautifulSoup

url ="http://securitytube.net/video/3000"
response = urllib.urlopen(url)
html = response.read()
bs = BeautifulSoup(html, 'lxml')

# bs = BeautifulSoup(html, 'lxml').read() is the same

# find <description> tag and its content

#description = bs.find('div', id='description')
description = bs.find('p', align='justify')
print description
print 
print description.string
print
print description.get_text()

# all links in description
print description.find_all('a') 
print

# get a video link
videoLink = bs.find('iframe', {'title':'YouTube video player'}) # could add multiple characteristics to the dictionnary in case one of them was shared by multiple objects
print videoLink
print videoLink['src']
print

# find all the form fields
forms = bs.find_all('form')
print forms
# not such a good way ...
