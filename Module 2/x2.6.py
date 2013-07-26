#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2 - Part 6'
print	'Exercice'
print

"""
Create a TCP server which listens to a port
Implement signals to ensure it automatically shuts down after a pre-configured duration, which is given via command line, eg :
tcp-server -s 100
shutdown after listenig to port for 100 seconds
"""


import signal
import sys
import SocketServer

killTIme = int(sys.argv[1])


# # #


# signal handler
def kill_server_handler(signal, frame) :
	print "Shutting down server"
	sys.exit(0)

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


# # #


serverAddress = ('0.0.0.0', 9000)

# specify type of server, address it is listening on and what to do once you get a connection (handle the connections)
server = SocketServer.TCPServer(serverAddress, EchoHandler)

# define what happens when a signal alarm is called
signal.signal(signal.SIGALRM, kill_server_handler)
signal.alarm(killTIme)

# could handle individual connections but in this case we just listen forever
server.serve_forever()
