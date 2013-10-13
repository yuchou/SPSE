#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 3'
print	'Network Security'
print	'Part 6 & 7'
print

"""
Scapy :
http://www.secdev.org/projects/scapy/demo.html
http://www.secdev.org/projects/scapy/doc/usage.html

Packet sniffing with scapy

sniff : sudo tcpdump -i eth0 -XX -vvv icmp
"""

# run dynamic scapy

ls() # protocols supported
conf # config options
lsc() # list command options

# finding protocols and details
ls(IP)	
IP().show()

# sniffing packets
pk = sniff(iface='eth0', count=3) # count - # of packets to sniff

pk
pk[0]
pk[0].dst
pk[0].show()

# dump the packets in hex
hexdump()
hexdump(pk[1])

# simulating sniffing with a offline pcap capture
pk = sniff(offline='offline.pcap')

# adding filters
# supports BPF (Berkley Packet Filters) out of the box
pk = sniff(iface='eth0', filter='arp', count=3)

# print packets as they come in
# lambda functions, prints a summary of the packets as they are captured
pk = sniff(iface='eth0', filter='icmp', count=20, prn=lambda x: x.summary())
pk = sniff(iface='eth0', prn=lambda x: x.show())

# write packets to a pcap file	
wrpcap()
wrpcap('demo.cap', pk)
# read pcap file
rdpcap()
pk = rdpcap('demo.cap')
pk

# put packets in string
icmp_str = str(pk[0])
# reconstruct packet (have to know the type of outermost protocol)
pk = Ether(icmp_str)

# export packets as Base64 encoded
export_object(str(pk[0])
# import packet from Base64
new_pk = import_object() # waits for input
[paste pk ]
new_pk
Ether(new_pk)

"""
Packet Injection with Scapy
"""

# creating packets
pk = IP(dst='google.com')
pk = IP(dst='google.com') /ICMP()
pk = IP(dst='google.com') /ICMP()/'Packet content'

# sending packets
#	-> layer 3 sending, routing according to local table
send(pk)

#	-> layer 2 sending, need to specify interface
# scapy injection and forging
# loop = keep sending
# inter = interval between packets (seconds)
sendp(Ether()/IP(dst='google.com')/ICMP()/'XXX', iface='eth0', loop=1, inter=1)

# send and receive
#	-> layer 2
srp1(Ether()/IP(dst='google.com', ttl=22)/ICMP()/'XXX')
r1(IP(dst='google.com'), timeout=3)

#	-> layer 3
#		-> sr() returns answer and unanswered packets
sr(IP(dst='google.com')/ICMP()/'XXX')
(response, no_response) = sr(IP(dst='google.com')/ICMP()/'XXX')
response[0]

# exit from the function if we get no reply after 5 seconds
sr(IP(dst='google.com'), timeout=5)

#		-> sr1() returns only answer or sent packets, waits for a single answer
sr1(IP(dst='google.com')/ICMP()/'XXX')

# routing (does not  touch to the actual computer's routing table)
conf.route # coupy the whole routing table from the computer
# add your own route
conf.route.add(host='192.168.0.100', gw='192.168.1.22')
conf.route.add(net='192.1.10.1/8', gw='192.168.1.22')
conf.route.resync() # reset
