#!/usr/bin/env python

import datetime
import cgi, cgitb
import Cookie
import os

cgitb.enable()

print "Content-type: text/html"


def inputNameForm():
	print """
	

	<html>
	<head><title>Name input form</title></head>
	<body>
	<form method='post'>
	<h3>What is your name my friend?</h3>
	<br/>
	<input name='yourname' type='text'>
	</input>
	<input type='submit' value='Answer'/>
	</form>
	</body>
	</html>
	"""

def greetingForm(value):
	print """	
	<html>
	<head><title>Greeting form</title></head>
	<body>
	"""
	print "<h3>Welcome %s!</h3><br/>"%value
	print "Current server date and time are"

	print datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

	print """
	</body>
	</html>
	"""

def getCookie():
	value = None
	
	try:	
		cookie = Cookie.SimpleCookie()
		cookie.load(os.environ.get('HTTP_COOKIE'))
		value = cookie['yourname'].value
	except:
		pass
	
	return value

def setCookie(value):
	cookie = Cookie.SimpleCookie()
	cookie['yourname'] = value
	print cookie
	print


val = getCookie()
if val != None:
	print
	greetingForm(val)
else:
	form = cgi.FieldStorage()
	name = form.getvalue('yourname')
	if name == None:
		inputNameForm()
	else:
		setCookie(name)
		greetingForm(name)
