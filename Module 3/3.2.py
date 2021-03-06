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
print	'Part 2'
print

"""
SocketServer framework
Enables to build tcp and udp servers, all the listening and connecting is taken care of by the framework

"""

#import socket
import SocketServer

# has to be a subclass of BaseRequestHandler
class EchoHandler(SocketServer.BaseRequestHandler) :
	# override handle to process request
	def handle(self) :
		print "Got connection from : ", self.client_address
		data = 'dummy'
		while len(data):
			data = self.request.recv(1024) # self.request is the client socket
			print 'Received : ', data
			self.request.send(data)
		print 'Client left.'

serverAddress = ('0.0.0.0', 9000)

# specify type of server, address it is listening on and what to do once you get a connection (handle the connections)
server = SocketServer.TCPServer(serverAddress, EchoHandler)

# could handle individual connections but in this case we just listen forever
server.serve_forever()


