#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                             "

print	'Part 1'
print	'Introduction to Python and Setting up an Environment'
print	'Module 7 - classDemo'
print

class Calculator:
	def __init__(self, inA, inB): # constructor => __ not _
		self.a = inA
		self.b = inB
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b

class scientificCalculator(Calculator):
	def power(self):
		return pow(self.a, self.b)

def quickAdd(a,b):
	return a+b
