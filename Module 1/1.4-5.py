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
print	'Module 4'

# if

val = 5 # int(raw_input("Enter a number : "))
if val==1:
	print 'a'
elif val==2:
	print 'b'
else:
	print 'c'

# while

sum = 10 # raw_input("Enter sum : ")
while sum<10:
	print sum
	if sum==1:
		break
	elif sum==3:
		continue
	else:
		pass
	sum+=1
print sum

# break : get out of innermost loop
# continue : start the next pass of the innermost loop
# pass : do nothing, placeholder

a = 4
while a<10:
	a+=1
else:
	print a

# for

sum=0
for i in range(10):
	sum+=i
print sum

aList = [('xav',10),('jav',15)]
for (x,y) in aList:
	print (x,y) 

bList = ['a', 2, [1,2]]
for something in bList:
	print something

for i in range(1,10,2):
	pass
else:
	print i

print range(10)
print range(1,10,2)

# functions

def myfunc(a, b):
	print a+b

myfunc(1,2)

"""
#!/usr/bin/python

def print5times(line):
	for i in range(5):
		print line

print5times(sys.argv[1])
"""
