#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 3'
print	'Network Security'
print	'Exercice'
print

"""
Find a class to run CGI scripts. Write a POC

go to
http://localhost:10000/cgi-bin/script.cgi

CGI scripts must be executable
"""

import SocketServer
import CGIHTTPServer

class CGIHTTP_requestHandler(CGIHTTPServer.CGIHTTPRequestHandler) :

        # cgi_directories = ["/cgi-bin"]

	def do_GET(self) :
	        self.server.server_name = 'localhost' 
		self.server.server_port = '10000'
		CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)

serverAddress = ('0.0.0.0', 10000)

http_server = SocketServer.TCPServer(serverAddress, CGIHTTP_requestHandler)

# start the server
http_server.serve_forever()

