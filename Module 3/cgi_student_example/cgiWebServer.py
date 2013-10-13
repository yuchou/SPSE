#!/usr/bin/env python

import SocketServer
from BaseHTTPServer import HTTPServer
import CGIHTTPServer

class  myCGIRequestHandler(CGIHTTPServer.CGIHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/admin' :
			self.wfile.write(" The page is accessible only for Admins\n")
			self.wfile.write(self.headers)

		else:
			CGIHTTPServer.CGIHTTPRequestHandler.do_GET(self)

	def do_POST(self):
		CGIHTTPServer.CGIHTTPRequestHandler.do_POST(self)
	
	def do_HEAD(self):
		CGIHTTPServer.CGIHTTPRequestHandler.do.HEAD(self)

httpServer = HTTPServer(("192.168.2.8",9001),myCGIRequestHandler)
httpServer.cgi_directories = "cgi-bin"
httpServer.serve_forever()

