#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Part 1'
print	'Python Language Essentails'
print	'Module 9'
print

# handling any exception

inputValue = int(raw_input("Enter number : "))
inputDivider = int(raw_input("Enter divider : "))

"""
# version 1
try :
	finalValue = inputValue/inputDivider
except : # exception happened
	print "There was an exception!\n"
	finalValue = 0
else : # exception did not happen (success)
	print "There was no exception!\n"
finally :  # always runs
	print "All ny cleanup goes here."
	print "The final value is : %s\n" %hex(finalValue)
"""

"""
# version 2
try :
	finalValue = inputValue/inputDivider
except  ZeroDivisionError:
	print "You cannot divide by zero!\n"
	finalValue = 0
except  : 
	print "There was an exception!\n"
	finalValue = 1
else :
	print "There was no exception!\n"
finally : 
	print "All ny cleanup goes here."
	print "The final value is : %d\n" %finalValue
"""

# version 3
try :
	finalValue = inputValue/inputDivider
except  Exception as details: # this value can be found in the dynamic interpreter by triggering the exception
	print details
	finalValue = 0
else :
	print "There was no exception!\n"
finally : 
	print "All ny cleanup goes here."
	print "The final value is : %d\n" %finalValue

