#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 7'
print	'Part 1'
print

"""
Automation with pexpect

The goal is not to replace a lib made especifically to interact with a program but to use one that can work with any program as long as we know how it works.

Vivek's example for ftp :

id = pexpect.spawn('ftp localhost')
id = pexpect._exact('Name')
id.sendline('demo')
id.expect_exact('Password')
id.sendline('demo123')
id.expect_exact('ftp')
id.sendline('ls')
id.expect_exact('ftp')
for line in lines :
		print line
"""

import pexpect
import sys

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
command = sys.argv[4]

PROMPT = ['# ', '>>> ', '> ','\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT) # any element from the list
    print child.before # response to expect

def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey,\
                        '[P|p]assword:'])
    
    if ret == 0:
        print '[-] Error Connecting'
        return
    
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
                            '[P|p]assword:'])
        if ret == 0:
            print '[-] Error Connecting'
            return
    
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    
    child = connect(user, host, password)
    send_command(child, command)

if __name__ == '__main__':
    main()
