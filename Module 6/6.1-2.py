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
print	'Part 1-2'
print

"""
Module 6.1
Portable Executable Basics

When PE files are loaded into memory via the Windows loader, the in-memory version is known as a module. The starting address where the file mapping begins is called an HMODULE. 

The linker takes all the sections named .text from the various OBJ files and combines them into a single .text section in the PE file. Likewise, all the sections named .data from the various OBJs are combined into a single .data section in the PE file.

Consider an EXE file loaded at address 0x400000, with its code section at address 0x401000 :

load address / HMODULE		0x400000  
RVA				0x001000
VA / target address 		0x401000 


PEfile
	https://code.google.com/p/pefile/

PEfile supports parsing PEiD's signatures. Comprehensive signature datbases can be found at:
http://bob.droppages.com/Projects/PEiD/PEiD+Plugins
	https://code.google.com/p/pefile/wiki/PEiDSignatures

"""

import pprint # Vivek uses pprint : useful to find field names 

import pefile
import peutils # module inluded in pefile

# in windows : c:\\windows\\path\\to\\file\\file.exe

filename = "files/image.dll"
filename = "files/reverseMe.exe"
filename = "files/reverseMe-packed.exe"

pe =  pefile.PE(filename)

"""
print "Raw output \n"
print pe
"""

"""
# dump of everything found
print pe.dump_info()
"""

print "PPrint output \n"
#pprint.pprint(dir(pe))
print


"""
print pprint.pprint(dir(pe.DOS_HEADER))
print
print hex(pe.DOS_HEADER.e_magic)
print hex(pe.DOS_HEADER.e_lfanew)
print

print pprint.pprint(dir(pe.FILE_HEADER))
print
print pe.FILE_HEADER.NumberOfSections
print

print "Iterating through the sections \n"
for section in pe.sections:
	name = str(section.Name)
	size = str(section.SizeOfRawData)
	print "%s - %s" %(name,size)
print
"""

"""
print
print "Listing the imported symbols"
for entry in pe.DIRECTORY_ENTRY_IMPORT:
	print
	print entry.dll
	for imp in entry.imports:
		print '\t', hex(imp.address), imp.name

if filename[len(filename)-3:len(filename)] == "dll" : # .exe have no exported functions
	print
	print "Listing the exported symbols \n"
	for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
		print hex(pe.OPTIONAL_HEADER.ImageBase + exp.address), exp.name, exp.ordinal
	print
"""

# analyse packed file
for sections in pe.sections :
	print sections.Name
print

# find type of packer used

# load a signature database
signatures = peutils.SignatureDatabase('files/UserDB.TXT')
# could also load a database directly from a URL :
# signatures = peutils.SignatureDatabase('https://reverse-engineering-scripts.googlecode.com/files/UserDB.TXT')

# Once we have a SignatureDatabase instance, we can run PE instances through it in order to find 
# matching packer signatures:
matches = signatures.match(pe, ep_only = True)
print matches
print





