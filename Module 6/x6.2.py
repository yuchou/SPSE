#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 6'
print	'Part 2'
print	'Exercice'
print

"""
Take a .exe and look if it imports a given .dll, then print the imports. Will check with an included and not included library.
"""

import pefile

def imports_lib(executable, library) :
	for lib in executable.DIRECTORY_ENTRY_IMPORT:
		if lib.dll == library :
			return True
	return False

def printIfImported(executable, library):
	if imports_lib(executable, library) == True :
		print "Library : %s" %library
		for entry in executable.DIRECTORY_ENTRY_IMPORT:
			if entry.dll == library :
				for imp in entry.imports:
					print '\t', hex(imp.address), imp.name
		print
	else :
		print '\t',"Not imported \n"

goodLibrary = "image.dll"
badLibrary = "DLL3.dll"

executable = pefile.PE("files/VisualSite Designer.exe")

print "Good library"
printIfImported(executable, goodLibrary)

print "Bad library"
printIfImported(executable, badLibrary)

