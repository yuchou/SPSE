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
print	'Exercice'
print

"""
Explore the concept of cookiejar - why is it useful - sample code
Usefull to share cookies between various instances of mechanize.

[ Explore http://seleniumhq.org/support/ - automate the current example in it ]

HTML view (no ajax) : 
assert br.viewing_html()

Use proxy : 
br.set_proxies({"http": "joe:password@myproxy.example.com:3128", "ftp": "proxy.example.com",})
br.add_proxy_password("joe", "password")
"""

import sys
import mechanize
import cookielib
from bs4 import BeautifulSoup

#####################
# variables			#
#####################

dvwa = 'http://172.16.28.128/dvwa/login.php'
sqli_url = 'http://172.16.28.128/dvwa/vulnerabilities/sqli/'

# # # # create browser object
browser1 = mechanize.Browser()
browser2 = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
browser1.set_cookiejar(cj)

#####################
# Functions			#
#####################

def dvwa_login(url, form, username, password) :
	
	browser1.open(url)
	print 'Loging into : ', str(browser1)
	
	# select the form to fill out
	browser1.select_form(nr=form) 
	browser1.form['username'] = username
	browser1.form['password'] = password
	browser1.submit()

#####################
# Main				#
#####################

# go to site
browser1.open(dvwa)
print 'Visiting : ', browser1.title()
# login
dvwa_login(dvwa, 0, 'admin', 'password')
print 'Visiting : ', browser1.title()

print
print 'Coockies : '
for cookie in cj :
	print cookie
print

# blocked (no cookie)
browser2.open(sqli_url)
print 'Visiting : ', browser2.title()

browser2.set_cookiejar(cj)

# allowed (shared cookie)
browser2.open(sqli_url)
print 'Visiting : ', browser2.title()


