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
print

"""
Write a pyCommand script to find if the DEP, ASLR, SafeSEH modules are enabled
"""

import immlib
import struct

DESC = "DEP, ASLR and SafeSEH Detection in all Modules"

# More information
# http://msdn.microsoft.com/en-us/library/windows/desktop/ms680339(v=vs.85).aspx
# How to detect presence of security mechanisms

IMAGE_DLLCHARACTERISTICS_NX_COMPAT = 0x0100  # DEP compatible
IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE = 0x0040 # ASLR 

def main(args) :

    imm = immlib.Debugger()

    # code borrowed from safeseh pycommand
    
    allmodules=imm.getAllModules()

    for key in allmodules.keys():
        dep = aslr = "NO"
        module = imm.getModule(key)
        module_baseAddress = module.getBaseAddress()
        pe_offset = struct.unpack('<L',imm.readMemory(module_baseAddress + 0x3c,4))[0]
        pebase = module_baseAddress + pe_offset
        flags = struct.unpack('<H',imm.readMemory(pebase + 0x5e,2))[0]

        if (flags & IMAGE_DLLCHARACTERISTICS_NX_COMPAT != 0) :
            dep = "YES"

        if (flags & IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE != 0) :
            aslr = "YES"

        imm.log("----  %s  ----" %key)
        imm.log("DEP: %s ASLR: %s" %(dep, aslr))
        imm.log("--------------")

    return "[+] Executed Successfully"
