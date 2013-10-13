#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 5'
print	'Exploitation Techniques'
print	'Part 2 and 3'
print

"""
IDB basics

IDB scripting with python
PyCOmmands :
	regular scripts which have to determine a main() function and return a string
	may have arguments

Documentation : Documentation/Ref/index.html
Cheatsheet : 
http://www.corelan.be/index.php/2010/01/26/starting-to-write-immunity-debugger-pycommands-my-cheatsheet/
"""

# PyCommand script
import immlib

DESC = 'Test script.'
def main(args) :
	imm = immlib.Debugger() # debugger to attach to the current instance
	imm.log('Done in log.') # return to log window	
	imm.updateLog() # otherwise it will wait till the whole code has been run to print
	return 'Done in bar.' # return to result bar

# # # run in console
# In the shell, immlib is already instantiated and imm is the name of the instance

imm.log('Done in log.')
imm.ps()

# put content inside a table
# create a table and priht the details

# table name | columns
# check documentation for fields
table = imm.createTable('SPSE Course', ['PID', 'Name', 'Path', 'Service'])

# get list of processes
psList = imm.ps()

# fill table
for process in psList :
	table.add(0, [str(process[0]), process[1], process[2], str(process[3])])

return 'Done.'
