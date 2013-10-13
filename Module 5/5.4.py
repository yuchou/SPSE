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
print	'Part 4'
print

"""
Playing with processes in IDB
"""

import immlib

imm = immlib.Debugger()

# # # # Main application

DESC = 'Playing with processes'
def main(args):


	# open closed process
	#exe = 'E:\\Module 6\\Server-Strcpy.exe'
	#imm.openProcess(exe) 

	# attach to running process - not the one opened in immunity
	# -> !script_name PID
	#imm.Attach(int(args[0])) #PID
	#imm.restartProcess()

	# find all modules in running process
	modules_table = imm.createTable('Module Information', ['Name', 'Base', 'Entry', 'Size', 'Version'])

	# get list of modules
	module_dict = imm.getAllModules()

	# fill table
	for entity in module_dict.values() :
		# Libs.debugtypes => Module
		modules_table.add(0, [
			entity.getName(),
			'%08X'%entity.getBaseAddress(),
			'%08X'%entity.getEntry(),
			'%08X'%entity.getSize(),
			entity.getVersion()
			])

	# print the state of registers in logs
	imm.log(str(imm.getRegs()))

	return 'Done'
