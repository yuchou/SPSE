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
FastLogHook/STDCALLFastLogHook

Create a hook for the strcpy() function which prints the arguments passed. (as in x5.6_1.py)

Uses injection hooking and does not need a debugger
Inject your own code and redirect control
Finish logging and return to normal flow

That way you don't have to break everytime the function is called.
"""

############################################
# GET ERROR WHEN RUNNING
############################################

import immlib

DESC = 'FastLogHook Demo'
NAME = 'StrcpyFastLogHook'

#-----------------------#
# Main					#
#-----------------------#

def main(args) :
	imm = immlib.Debugger()

	# check knowledgebase to see if there is an entry for the name
	fastHook = imm.getKnowledge(NAME)
	# if exists, print all the results
	if fastHook :
		loggingResults = fastHook.getAllLog()
		imm.log(str(loggingResults))

		# parse the results
		(functionAddress, (esp, esp_4, esp_8)) = loggingResults[0]
		dataReceived = imm.readString(esp_8) # same as strcpy_source
		imm.log(dataReceived)

		return '[+] Finished fetching results'

	# find strcpy address
	functionToHook = 'msvcrt.strcpy'
	functionAddress = imm.getAddress(functionToHook)
	# install FastLogHook
	fastHook = immlib.FastLogHook(imm)
	# log interesting content
	fastHook.logFunction(functionAddress)
	fastHook.logBaseDisplacement('ESP', 0)
	fastHook.logBaseDisplacement('ESP', 4)
	fastHook.logBaseDisplacement('ESP', 8)

	fastHook.Hook()
	# add what we found to the knowledgebase
	imm.addKnowledge(NAME, fastHook, force_add=1)

	return '[+] Done'
