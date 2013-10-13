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
print	'Part 3'
print

"""
SimpleHTTPServer class to make HTTP servers on the fly

"""

import SocketServer
import SimpleHTTPServer

class HTTP_requestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler) :
	def do_GET(self) :
		# page : http://localhost:10000/admin
		if self.path == '/admin' :
			self.wfile.write('This page is only for 1337s.\n')
			self.wfile.write(self.headers) # headers sent by client to server
		else :
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

serverAddress = ('0.0.0.0', 10000)

# pass ip, port and request handler
# all the connection management is outsourced and we only take care of the request itself
http_server = SocketServer.TCPServer(serverAddress, HTTP_requestHandler)
# start the server
http_server.serve_forever()
