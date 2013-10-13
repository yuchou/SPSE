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
print

"""
Catch all send/recv calls and print the arguments (look in MSDN)

Create API monitor for
- registry writes to 'run on login' and 'run on boot'
- opening / writing / reading files
- send/recv on network

Understanding send/recv :
http://www.scottklement.com/rpg/socktut/sendrecvapi.html

complete other functions :
http://student.securitytube.net/mod/forum/discuss.php?d=811
"""

# imports
import struct
import sys

from pydbg import *
from pydbg.defines import *

# global variables
process = 'strcpy_server.exe'
line = '----------------------------------'

# breakpoint handlers

def send_bp(dbg):
	print line
	print '#\tsend() call\t#'
	esp = dbg.context.Esp
	# sock_desc
	arg1 = dbg.read_process_memory(esp+0x4, 4) 
	arg1 = struct.unpack("L",arg1)[0] 
	print 'socket description : %s' %str(arg1)
	# buffer
	arg2 = dbg.read_process_memory(esp+0x8, 4) # get buffer address (4 bytes)
	arg2 = struct.unpack("L",arg2)[0] # format to read
	arg2 = dbg.read_process_memory(int(arg2), 100) # read 100 chars from start of buffer address
	arg2 = dbg.get_ascii_string(arg2) # transform buffer to string
	print 'buffer content : %s' %arg2
	# buffer_len
	arg3 = dbg.read_process_memory(esp+0xC, 4)
	arg3 = struct.unpack("L",arg3)[0]
	print 'buffer length : %s' %str(arg3)
	# flags
	arg4 = dbg.read_process_memory(esp+0xF, 4)
	arg4 = struct.unpack("L",arg4)[0]
	print 'flags : %s' %str(arg4)
	# keep running
	return DBG_CONTINUE

def recv_bp(dbg):
	print line
	print '#\trecv() call\t#'
	esp = dbg.context.Esp
	# sock_desc
	arg1 = dbg.read_process_memory(esp+0x4, 4) 
	arg1 = struct.unpack("L",arg1)[0] 
	print 'socket description : %s' %str(arg1)
	# buffer
	arg2 = dbg.read_process_memory(esp+0x8, 4) # get buffer address (4 bytes)
	arg2 = struct.unpack("L",arg2)[0] # format to read
	arg2 = dbg.read_process_memory(int(arg2), 100) # read 100 chars from start of buffer address
	arg2 = dbg.get_ascii_string(arg2) # transform buffer to string
	print 'buffer content : %s' %arg2
	# buffer_len
	arg3 = dbg.read_process_memory(esp+0xC, 4)
	arg3 = struct.unpack("L",arg3)[0]
	print 'buffer length : %s' %str(arg3)
	# flags
	arg4 = dbg.read_process_memory(esp+0xF, 4)
	arg4 = struct.unpack("L",arg4)[0]
	print 'flags : %s' %str(arg4)
	# keep running
	return DBG_CONTINUE

# global debugger object
dbg = pydbg()

# list all processes and find the one we want
found = False
for pid, name in dbg.enumerate_processes() :
	if process == name :
		dbg.attach(pid)
		found = True
		print "[+] Attached to process %s with PID %s" %(name, str(pid))
		break
if not found :
	print "[-] Process not found. Exiting"
	exit(1)

# find function addresses
send_address = dbg.func_resolve('ws2_32', 'send')
recv_address = dbg.func_resolve('ws2_32', 'recv')

#RegCKey_ExW_address = dbg.func_resolve("advapi32","RegCreateKeyExW")
#RegCKey_ExA_address = dbg.func_resolve("advapi32","RegCreateKeyExA")
#RegSVKey_ExW_address = dbg.func_resolve("advapi32","RegSetValueExW")
#RegSVKey_ExA_address = dbg.func_resolve("advapi32","RegSetValueExA")

#RFile_address = dbg.func_resolve("kernel32","ReadFile")
#WFile_address = dbg.func_resolve("kernel32","WriteFile")

#CFile_W_address = dbg.func_resolve("kernel32","CreateFileW")
#CFile_A_address = dbg.func_resolve("kernel32","CreateFileA")

# set breakpoint on function addresses
dbg.bp_set(send_address, description='send BP', handler=send_bp)
dbg.bp_set(recv_address, description='recv BP', handler=recv_bp)

#dbg.bp_set(RegCKey_ExW_address, description='RegCreateKeyExW BP', handler=RegCreateKeyExW_bp)
#dbg.bp_set(RegCKey_ExA_address, description='RegCreateKeyExA BP', handler=RegCreateKeyExA_bp)
#dbg.bp_set(RegSVKey_ExW_address, description='RegSetValueExW BP', handler=RegSetValueExW_bp)
#dbg.bp_set(RegSVKey_ExA_address, description='RegSetValueExA BP', handler=RegSetValueExA_bp)

#dbg.bp_set(RFile_addr, description='ReadFile BP', handler=RFile_bp)
#dbg.bp_set(WFile_addr, description='WriteFile BP', handler=WFile_bp)

#dbg.bp_set(CFile_W_address, description='CFileW BP', handler=CFileW_bp)
#dbg.bp_set(CFile_A_address, description='CFileA BP', handler=CFileA_bp)

# run debugger
dbg.run()








