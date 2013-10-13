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
Read through the documentation  of BeautifulSoup 4 and find other ways to iterate through tags and get to the juicy information.

http://www.crummy.com/software/BeautifulSoup/bs4/doc/

Not much of an exercice ... 

"""

from bs4 import BeautifulSoup
import urllib

html = urllib.urlopen('http://www.securitytube.net/video/7313')
htmlDom = BeautifulSoup(html)

allComments = htmlDom.find_all('ul', class_='comments')
print allComments
print allComments[0].get_text()


