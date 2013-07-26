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
print	'Module 7'
print

import classDemo
# from classDemo import scientificCalculator

print 'quickAdd a+b : %d' %classDemo.quickAdd(4,5)

newCalculator = classDemo.Calculator(3,2)
newScientificCalculator = classDemo.scientificCalculator(2,4)

print newCalculator.add()
print newScientificCalculator.power()

