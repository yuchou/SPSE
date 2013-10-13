#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 2'
print	'System Programming'
print	'Part 7'
print

"""
Unables us to invoque other processes and interract with them

The use of the shell=True argument in calling a subprocess allows the code to execute within a shell.  By invoking a shell, any program may be executed. Using this feature will allow for the expansion of environment variables and file globs.  The vulnerability is command injection to occur when using untrusted input and greatly increases risk to the system becasue of this use of untrusted input. 


"""

import subprocess

#subprocess.call(['ps','aux'])

print subprocess.call(['ls','-l']), '\n'
print subprocess.check_output(['ls', '-s'])

line =  subprocess.check_output(['ls'])
#print line
line_list = line.split('\n')

for line in line_list :
	print line

# map the stdin/stdout/stderror of the invoqued subprocess to use it in the program
handle = subprocess.Popen('ls', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

print handle.stdout.read()
