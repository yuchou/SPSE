#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 7'
print

"""
ssh automation with paramiko
easy creation of ssh and sftp clients
"""

import paramiko
import sys

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

# client object
ssh = paramiko.SSHClient()

# what to do when there is no key is present
# does not accept leys by default
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, username=user, password=password)

command = 'placeholder'

while command :
	command = raw_input('# ')

	# map the process
	(stdin, stdout, stderr) = ssh.exec_command(command)

	for line in stdout.readlines() :
		print line.strip()

ssh.close()


