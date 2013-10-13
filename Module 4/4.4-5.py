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
print	'Part 4 & Part 5'
print

"""
Form parsing and submission

In mechanize we simulate a browser (can even go back in history)

Stateful web browsing with mechanize

Examples :
http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/

HTTP Error 403: request disallowed by robots.txt
web servers have the ability to return a 403 based on the User-Agent attribute of the HTTP header sent with your request. In order to have your script mimic a browser, you have to miss-represent yourself. Meaning, you need to change the HTTP header User-Agent attribute to be the same as the one used by a mainstream web browser (e.g., Firefox, IE, Chrome). Right now it probably says something like 'Mechanize'.

"""

import mechanize

# # # #

username = 'notmyname'
password = 'notmypass'

good_response = '<Browser visiting http://www.enigmagroup.org/forums/index.php>'
bad_response = '<Browser visiting http://www.enigmagroup.org/forums/index.php?action=login2>'

url = "http://securitytube.net/video/3000"
url = 'http://www.enigmagroup.org/'

# # # #

browser = mechanize.Browser()
browser.open(url)
print browser
print

for form in browser.forms() :
	print form
	print

# select the form to fill out
browser.select_form(nr=0) # second form 0,1,2,...
# all activities will then happen in that form context
browser.form['q'] = 'defcon'
browser.submit()

for link in browser.links() :
#	print dir(link)
	print link.text
	print link.absolute_url
	print


"""
browser.select_form(nr=1) 
browser.form['user'] = username
browser.form['passwrd'] = password
browser.submit()

if str(browser) == good_response :
	print 'Logged in. \n'
elif str(browser) == bad_response :
	print 'Bad credentials \n'
else :
	print 'Error'
"""

# # # # part 5

# # # # variables

url = 'http://www.enigmagroup.org/'

# # # #

browser.open(url) 

#for link in browser.links() :
#	print link.text

new_link = browser.click_link(text='Tools') # find the link using the text value
browser.open(new_link)
print browser.response().read() # show html content















