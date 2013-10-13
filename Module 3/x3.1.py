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
print	'Part 1'
print

"""
1) make server multi-threaded 						(x)
2) make server multi-processed						(x)
3) create non-blocking multiplexed echo server using Select()		( )
		http://www.ibm.com/developerworks/linux/tutorials/l-pysocks/section4.html
		http://ilab.cs.byu.edu/python/select/echoserver.html

http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
"""

import socket
import threading

# Our thread class:
class ClientThread ( threading.Thread ):

	# Override Thread's __init__ method to accept the parameters needed:
	def __init__ ( self, client, (ip, port) ):
		threading.Thread.__init__ ( self )
		self.client = client
		self.ip = ip
		self.port = port

	def run ( self ):
		print 'Received connection: %s' %ip
		self.client.send ( "Welcome %s \n" %ip )
		data = 'data'
		while len(data) : # keep echo while not zero
			data = client.recv(2048) # receive 2048 bytes from client
			print "%s : %s " %(ip, data)
			client.send("You sent : "+data)
		self.client.close()
		print 'Closed connection: %s' %ip

# Set up the server:
server = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
# assure that if the server disconnects, the address is again available quickly
server.setsockopt ( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 )
server.bind ( ( '', 8009 ) )
# number of concurrent clients the socket can handle
server.listen (5)

# Have the server serve "forever":
while True:
	(client, (ip, port)) = server.accept()
	ClientThread ( client, (ip, port) ).start()





