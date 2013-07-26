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
print	'Module 6'
print

# classes and objects

class Calculator:
	def __init__(self, inA, inB): # constructor => __ not _
		self.a = inA
		self.b = inB
	def add(self):
		return self.a + self.b
	def sub(self):
		return self.a - self.b

newC = Calculator(3,2)

print 'a + b = %d' %newC.add()
print 'a - b = %d' %newC.sub()

# inheritance

class sciCalc(Calculator):
	def power(self):
		return pow(self.a, self.b)

newSciC = sciCalc(2,4)

print 'a^b = %d' %newSciC.power()

############################
print

class Container:
	a = 1
	b = 2
	c = 'wor'
	def __init__(self, obj):
		self.obj = obj
		self.b = obj

	
aContainer = Container([1,2])

print aContainer
print id(aContainer)
print aContainer.a
print aContainer.obj
print aContainer.b




