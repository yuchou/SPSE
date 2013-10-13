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
SFTP uses a ssh transport layer.
Enables remote upload/download
"""

import paramiko
import sys

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]

# same as ssh
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, username=user, password=password)

# become sftp
sftp = ssh.open_sftp()

# actions 
content = sftp.listdir()
print content
sftp.get(content[2], content[2])

# sftp.put('...', '...')

sftp.chdir('/')
print sftp.listdir()

ssh.close()
