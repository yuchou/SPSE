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
print	'Part 6'
print

"""
Hooks to manipulate a running program

[Can run them as individual hooks in the pyhook directory instead of in pycommand]

Create a hook as part of a pycommand : use this to analyse the crash 
	of the server when it receives a large buffer

"""

import immlib
from immlib import AllExceptHook # enables to deal with hooks

#-----------------------#
# Functions				#
#-----------------------#

def to_hex(intAddress):
   return "%08X" %intAddress

#-----------------------#
# Objects				#
#-----------------------#

class CatchHook(AllExceptHook) :
	
	def __init__(self) :
		AllExceptHook.__init__(self)

	# overload the run() command -> what happens when a object is instantiated
	# gets passed a dict of cpu registers
	def run(self, registers) :
		imm = immlib.Debugger()

		eip = to_hex(registers['EIP'])
		esp = to_hex(registers['ESP'])

		# printing the string available in ESP
		# [what if the string does not exits]
		imm.log("EIP : 0x%s ESP : 0x%s" %(eip, esp))

		# dump top of stack
		stack = imm.readString(esp) # address of string to read (top of stack)
		if stack :
			imm.log('String len at ESP : %d' %len(stack))
			imm.log('String value at ESP : %s' %stack)

#-----------------------#
# Main					#
#-----------------------#

def main(args) :

	imm = immlib.Debugger()
	imm.log('[+] Adding hook')

	# create instance of the hook class ; this hook will catch any exception
	newHook = CatchHook() 
	# add it to the list of hooks maintainted in the debugger
	newHook.add('Catch Hook') 

	return '[+] Done'
