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
print	'Part 5'
print

"""
Using IDB APIs to assemble, disassemble and search for different locations

Take as argument a set of instructions to search for in the program
Find the addressses and the modules
Create a table showing all of that
"""

import immlib

imm = immlib.Debugger()

# # # # interpreted code
'''
imm.assemble('jmp esp')
imm.assemble('jmp esp \n ret')

imm.disasm(0x00401267).getDisasm()

imm.search(imm.assemble('jmp esp \n ret'))
imm.search(imm.assemble('jmp esp'))

# find module in which address exists
imm.findModule(imm.search(imm.assemble('jmp esp'))[0])
'''

# # # # Main application

#-----------------------#
# Functions				#
#-----------------------#

def to_hex(intAddress):
   return "%08X" %intAddress

#-----------------------#
# Main					#
#-----------------------#

DESC = 'Search instructions and print in table'
def main(args):

	a = imm.findModuleByName('kernel32')
	

	if not args :
		return "[-] No instructions specified"

	instruction = ' '.join(args) 
	instruction = instruction.replace('/', '\n') # separate instructions with '/'
	assembled_instructions = imm.assemble(instruction)

	# search for instructions and return list containing addresses
	addressList = imm.search(assembled_instructions)

	table = imm.createTable('Instruction Locations', ['Module', 'Base Address', 'Instruction Address', 'Instruction'])

	for address in addressList :
		# Get module for this address
		module = imm.findModule(address)
		if not module :
			imm.log('Address : 0x%s not in any module' %to_hez(address))
			continue

		# [Get module object by name min12
		#	imm.findModuleByName('kernel32')
		
		# variables for double-check
		instruction = ''
		numArgs = len(' '.join(args).split('/'))

		# re-assemble the instruction to make sure it searched for what we wanted
		for count in range(0, numArgs) :
			# disassemble each instruction one after the other, moving from the base address
			# so basically it takes the address of the first instruction and the number of
			# subsequent instructions and disassembles them
			instruction += imm.disasmForward(address, nlines=count).getDisasm() + ' / '

		table.add(0, [
			module[0],
			str('%08X'%module[1]),
			str('%08X'%address),
			instruction
			])

	return '[+] Done'
