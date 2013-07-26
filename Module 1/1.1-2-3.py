#!/usr/bin/python
# #!/usr/bin/python3

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Part 1'
print	'Python Language Essentails'
print	'Modules 1,2,3'
"""

python-virtualenv - Python virtual environment creator

"""

# new line 
name = 'aa\nbb'
print name

# raw string
name = r'aa\nbb'
print name

# direct formating
name = """line 1
	line 2
line 3

line 4"""
print name

# unicode
name = u'jav'
print name

name = unicode('jav')
print name

# stings are immutable

name = 'jav'
print name[0]
# name[0] = 'v' <= error

# references
a = b = 'jav'
print hex(id(a))
print hex(id(b))

# concat
first = 'Javier'
second = 'Aranda'
full = first + ' ' + second
print full

# repeat
foo = 'ab'*10
print foo

# slice
print foo[0::2]

# string methods
name = 'javier'
print name.find('avier')
name2 = name.split('v')
print name2
name3 = name.replace('v','VVV')
print name3

# string formating
ip = '192.168.1.10'
num = 20
line = "Crack this : %s, %d times" %(ip,num)
print line 

# lists
print 
shortList = [1,2,3]
longList = ['jav', shortList, 999, ['aaa', 'bbb']]

print longList[1][2]
print longList[3][1]

print 'List length : %s' % len(longList)
print longList + shortList

longList.append(shortList)
print longList

longList.reverse()
print longList

longList.pop()
print longList

longList.extend([1,[9,8,9]])
print longList

longList.insert(1,'AAAAA')
print longList

del longList[1]
print longList

# tuples and lists
print
alist = ["SPSE intro", 23, 100, 3]
print alist
videoData = tuple(alist)
print videoData
videoTitle, runningTime, upVotes, downVotes, = videoData
print upVotes

# sets
setA = set([1,2,3,3])
print setA
setB = set([1,3,4])
print setB
print setA & setB
print setA | setB
print setA ^ setB
print setA - setB

# dictionnaries
myDict = dict(name='jav', age=22)
myDict['gender'] = 'male'
print myDict   

someDict = {}
someDict['bla'] = 1
someDict['bleh'] = 2
print someDict

oneDict = {'a':1, 'b':2}
print oneDict
print oneDict.has_key('a')
print 'c' in oneDict

print myDict.keys()
print myDict.items() # list of tuples
print myDict.values()
print myDict.get('name')

del myDict['name']
print myDict
myDict.clear()
print myDict

# get quick help
# dir(myDict)
# help(myDict.has_key)
