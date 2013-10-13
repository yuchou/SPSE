#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 4 - Part 3'
print	'Exercice'
print

"""
Write a scraper for a few websites to get the page and seach for specific content, then print it in a relevant manner

"""

import urllib
from bs4 import BeautifulSoup
import pprint
# Enigmagroups Recent Posts

url ='http://enigmagroup.org'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')

print soup.title
print soup.title.name

table = soup.find_all('tr', 'td')
post = table.find_all('td')

for i in post :
	print i



"""
#description = bs.find('div', id='description')
table = bs.find_all(table border='0', width='100%')

for el in table:
	print el

print table[2]
print table[2].string

print table[2].find_all('td')


#pprint.pprint(dir(table[9]))
"""

