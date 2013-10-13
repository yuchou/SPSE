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
Modify hidden fields to send arbitrary data
	=> browser.form.set_all_readonly(False)

OR

browser.select_form("form_name")

# writable field
field1 = browser.form.find_control('field1')
field1.value = ['newvalue']

# hidden field
field2 = browser.form.find_control('field2')
field2.readonly = False
field2.value = newvalue
field2.readonly = True

"""

import sys
import mechanize
import cookielib
from bs4 import BeautifulSoup

#####################
# variables			#
#####################

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
# Main				#
#####################

browser.open('http://www.google.com')

print('original page:')
for form in browser.forms():
    print(form)

# try to change the language; hl=nl field, readonly:
browser.select_form(nr=0)
# overwrite:
browser.form.set_all_readonly(False)
browser.form['hl']='fr'
browser.submit()

# check forms again to see if language has changed:
print('\npage with different language:')
for form in browser.forms():
    print(form)
