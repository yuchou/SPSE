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

# Write the return of ps() to a coma separated csv file
# The first row should be the table column names

#	Could use csv module
#	import csv
#	[...]
#	csvWriter = csv.writer(open(filename, "wb"))
#	csvWriter.writerow(["PID", "Process", "Path"])
#	[...]
#	for process in psList :
#		csvWriter.writerow([ str(process[0]), str(process[1]), str(process[2]) ])
#	[...]

#-----------------------#
# Global				#
#-----------------------#

import immlib

# import immutils
# from immutils import *

imm = immlib.Debugger()

#-----------------------#
# Functions				#
#-----------------------#

# write list content into csv file
def write_csv_line(textfile, PID, Name, Path, Service) :
	textfile.write('%s,%s,%s,%s\n' %(PID, Name, Path, Service))

#-----------------------#
# Main					#
#-----------------------#

DESC = 'Write the return of ps() to a csv'
def main(args):

	filename="ps_output.csv"
	textfile=open(filename,"w")

	# file header
	write_csv_line(textfile, 'PID', 'Name', 'Path', 'Service(s)')

	psList = imm.ps()
	# fill table
	for process in psList :
		write_csv_line(textfile, str(process[0]), process[1], process[2], str(process[3]))

	textfile.close()
	return '[+] Done'





