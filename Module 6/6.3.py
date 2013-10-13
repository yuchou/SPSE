#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 6'
print	'REverse Engineering'
print	'Part 3'
print

""" 
pydasm : a library to disassemble instructions

libdasm
http://code.google.com/p/libdasm/

Windows installer :
http://breakingcode.wordpress.com/2012/04/08/quickpost-installer-for-beaenginepython/

pydasm is the binding implementation to use libdasm (written in c)
The goal is to do 32bit disassembly using pydasm
install
http://www.glamenv-septzen.net/en/view/13
"""

import pydasm
import pprint

instruction = pydasm.get_instruction('\x50', pydasm.MODE_32)
# get instruction in assembly
print pydasm.get_instruction_string(instruction, pydasm.FORMAT_INTEL, 0)

instruction = pydasm.get_instruction("\x85\xC0", pydasm.MODE_32)
print pydasm.get_instruction_string(instruction, pydasm.FORMAT_INTEL, 0)
# AT&T syntax
print pydasm.get_instruction_string(instruction, pydasm.FORMAT_ATT, 0)

instruction = pydasm.get_instruction("\xC2\x04\x00", pydasm.MODE_32)
print pydasm.get_instruction_string(instruction, pydasm.FORMAT_INTEL, 0)

# objects contained in the module
pprint.pprint(dir(pydasm))
# what is available in the instruction object
pprint.pprint(dir(instruction))
print instruction.op1
