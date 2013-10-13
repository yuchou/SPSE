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
print	'Exercice'
print

"""
BpHook/LogBpHook

Create a hook for the strcpy() function which prints the arguments passed.

Enables a hook that puts a breakpoint when a function is called
Find address of strcpy in the program space
Create a BreakpointHook for that address
When that breaks, get the function arguments from the stack and then just print them out.
- Then do an analysis to predict an overflow.

LogBpHook will not call a Bp and will continue program flow so all we can do is log the data being passed to a funtion while it is being run.

"""

import immlib
from immlib import BpHook

#-----------------------#
# Functions				#
#-----------------------#

def to_hex(intAddress):
	return "%08X" %intAddress

#-----------------------#
# Objects				#
#-----------------------#

class strcpy_BpHook(BpHook) :

	def __init__(self) :
		BpHook.__init__(self)

	# overload the run() command -> what happens when a object is instantiated
	# gets passed a dict of cpu registers
	def run(self, registers) :
		imm = immlib.Debugger()
		imm.log('[+] strcpy BpHook called')
		
		# strcpy(char * destination, char * source)
		# get arguments on the stack (like in assembly)
		eipOnStack = imm.readLong(registers['ESP'])
		strcpy_destination = imm.readLong(registers['ESP'] + 4)
		strcpy_source = imm.readLong(registers['ESP'] + 8)

		imm.log('EIP on Stack : 0x%s' %to_hex(eipOnStack))

		# get the copied content of the call (string sent to the server)
		receivedString = imm.readString(strcpy_source)
		imm.log(receivedString)
		imm.log('Received string of lenght: %d' %len(reveivedString))
		imm.log('Received string : %s' %str(receivedString))

#-----------------------#
# Main					#
#-----------------------#

DESC = 'BPHook Demonstration'
def main(args) :
	imm = immlib.Debugger()

	# find strcpy address
	functionToHook = 'msvcrt.strcpy'
	functionAddress = imm.getAddress(functionToHook)

	# create instance of the hook class ; this hook will catch breakpoints 
	# for a given function and address
	newHook = strcpy_BpHook()
	# add it to the list of hooks maintainted in the debugger
	newHook.add(functionToHook, functionAddress)

	imm.log('Hook for %s : %s added' %(functionToHook, to_hex(functionAddress)))

	return '[+] Done'
