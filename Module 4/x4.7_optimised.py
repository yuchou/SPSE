#!/usr/bin/python
# -*- coding: utf-8 -*-

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 7'
print	'Attacking Web Applications'
print	'Exercice'
print

'''
Crawl a website for a certain defined depth.
Insert HTML into a MySQL database => will only insert url
Parse all forms and insert form fields in a per page basis 

MySQL 
http://zetcode.com/databases/mysqltutorial/
MySQL python
http://zetcode.com/db/mysqlpython/

sudo mysql
mysql> SHOW DATABASES;
mysql> CREATE DATABASE spse;
mysql> CREATE USER 'god'@'localhost' IDENTIFIED BY 'spsepass';
mysql> USE spse;
mysql> GRANT ALL ON spse.* TO 'god'@'localhost';
mysql> quit;
'''

from optparse import OptionParser

from time import time
import sys
import threading

from bs4 import BeautifulSoup
import urllib

import MySQLdb as handler

#-----------------------#
# Variables				#
#-----------------------#

usageString = "Usage: %prog [options]"
parser = OptionParser(usage=usageString)

parser.add_option("-d", "--database", dest="database", metavar="DATABASE", default='spse', type="string", 
	help="MySQL database in which to insert values")
parser.add_option("-u", "--user", dest="user", metavar="USER", default='test', type="string", 
	help="User for the MySQL database")
parser.add_option("-p", "--password", dest="password", metavar="PASSWORD", default='spsepass', type="string", 
	help="Password for the user of the MySQL database")
parser.add_option("-s", "--site", dest="base_url", metavar="BASEURL", default='http://google.com', type="string", 
	help="Base URL to crawl")
parser.add_option("-l", "--layer", dest="MAX_DEPTH", metavar="MAXDEPTH", default='1', type="int", 
	help="Number of layers to crawl (depth)")

(options,args) = parser.parse_args()

# more input than expected
if len(args) > 0:
	parser.error("Invalid additional option(s)")

# variables
database = options.database
user = options.user
password = options.password
base_url = options.base_url
MAX_DEPTH = options.MAX_DEPTH

# check that has all necessary values
if not database and not user and not password and not bid_base_url and not MAX_DEPTH :
	parser.error("Missing options")
if not database :
	parser.error("Missing database")
if not user :
	parser.error("Missing user")
if not password :
	parser.error("Missing password")
if not base_url :
	parser.error("Missing base URL")
if not MAX_DEPTH :
	parser.error("Missing max depth")

THREADS = []

#-----------------------#
# Functions				#
#-----------------------#

# takes a soup and returns a list of urls
def get_all_url(soup) :
	links = soup.find_all('a')
	all_url = []
	for link in links :
		try :
			if link['href'][0:4] == 'http' : # absolute path
				url = link['href']
				all_url.append(url)
			elif link['href'][0] == '/' : # relative path
				url = base_url+link['href']
				all_url.append(url)
			#else : # bad link ?
				#print link['href']
		except Exception, txt:
			pass
	return all_url

# takes a soup and returns a list of forms
def get_all_forms(soup) :
	forms = soup.find_all('form')
	all_forms = []
	for form in forms :
		all_forms.append(form)
	return all_forms

# takes a form list and returns a list of fields
def get_all_fields(forms) :
	all_fields = []
	for form in forms :
		fields = form.find_all('input')
		for field in fields :
			all_fields.append(field)
	return all_fields

# takes a url and returns the BeautifulSoup parsing result
def get_soup(url) :
	return BeautifulSoup(urllib.urlopen(base_url))

# takes a list of url and returns list of urls not yet in the db
def sanitize_url(all_url) :
	# remove doubles
	new_url = []
	for url in all_url :
		if url not in new_url :
			new_url.append(url)
	# remove already in db
	final_url = url_table_object.url_exists(new_url)
	return final_url

# craws a page and keeps going if max_depth not reached
def crawl_url(current_url, url_depth) :
	soup = get_soup(current_url)
	all_url = get_all_url(soup)
	all_forms = get_all_forms(soup)
	all_fields = get_all_fields(all_forms)
	form_table_object.add_element(current_url, all_fields)
	# keep crawling
	if url_depth < MAX_DEPTH :
		new_depth = url_depth+1
		all_new_url = sanitize_url(all_url)
		url_table_object.add_element(all_new_url, new_depth)
		'''
		# only thread first depth of search
		if url_depth == 0 :
			length = int(len(all_new_url)/5)
			thread1 = threading.Thread(target=crawl_url(all_new_url[0:length-1], new_depth))
			thread1.start()
			THREADS.append(thread1)
			thread2 = threading.Thread(target=crawl_url(all_new_url[length:2*length-1], new_depth))
			thread2.start()
			THREADS.append(thread2)
			thread3 = threading.Thread(target=crawl_url(all_new_url[2*length:3*length-1], new_depth))
			thread3.start()
			THREADS.append(thread3)
			thread4 = threading.Thread(target=crawl_url(all_new_url[3*length:4*length-1], new_depth))
			thread4.start()
			THREADS.append(thread4)
			thread5 = threading.Thread(target=crawl_url(all_new_url[4*length:], new_depth))
			thread5.start()
			THREADS.append(thread5)

			for thread in THREADS :
				thread.join()
		# other depths of search
		else :
			for url in all_new_url :
				crawl_url(url,new_depth)
		'''
		for url in all_new_url :
			crawl_url(url,new_depth)


#-----------------------#
# Objects				#
#-----------------------#

# This table contains : id+url+depth
class url_table :

	def __init__(self, database, table, user, password):
		self.database = database
		self.table = table
		self.user = user
		self.password = password
		# initialise table
		connection = self.connect()
		with connection:
			cursor = connection.cursor()
			cursor.execute("DROP TABLE IF EXISTS %s" %self.table)
		connection.close()

	def connect(self) :
		try :
			connection = handler.connect('localhost', self.user, self.password, self.database)
		except Exception, e :
			print e
			sys.exit(1)
		else :
			return connection

	def add_element(self, urlList, depth) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor()
			cursor.execute("CREATE TABLE IF NOT EXISTS %s(Id INT PRIMARY KEY AUTO_INCREMENT, URL VARCHAR(100), depth INT)" %self.table)
			for url in urlList :
				try :
					cursor.execute("INSERT INTO %s(URL, depth) VALUES(\'%s\',\'%s\')" %(self.table,url,depth))
				except Exception, txt :
					pass #print 'Error : ',txt
		connection.close()

	def get_table_elements(self) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor(handler.cursors.DictCursor)
			cursor.execute("SELECT * FROM %s" %self.table)
			return cursor.fetchall()
		connection.close()

	def url_exists(self, urlList) :
		new_url = []
		connection = self.connect()
		with connection:
			cursor = connection.cursor(handler.cursors.DictCursor)
			for url in urlList :
				try :
					exists = cursor.execute("SELECT URL FROM %s WHERE URL=\'%s\'" %(self.table, url))
					if not exists :
						new_url.append(url)
				except Exception, txt :
					pass #print 'Error : ',txt
		connection.close()
		return new_url

# This table contains : id+url+form_field
class form_table :

	def __init__(self, database, table, user, password):
		self.database = database
		self.table = table
		self.user = user
		self.password = password
		# initialise table
		connection = self.connect()
		with connection:
			cursor = connection.cursor()
			cursor.execute("DROP TABLE IF EXISTS %s" %self.table)
		connection.close()

	def connect(self) :
		try :
			connection = handler.connect('localhost', self.user, self.password, self.database)
		except Exception, e :
			print e
			sys.exit(1)
		else :
			return connection

	def add_element(self, url, fieldList) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor()
			cursor.execute("CREATE TABLE IF NOT EXISTS %s(Id INT PRIMARY KEY AUTO_INCREMENT, URL VARCHAR(100), field TEXT)" %self.table)
			for field in fieldList :
				try :
					cursor.execute("INSERT INTO %s(url, field) VALUES(\'%s\',\'%s\')" %(self.table,url,field))
				except Exception, txt :
					pass #print 'Error : ',txt
		connection.close()

	def get_table_elements(self) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor(handler.cursors.DictCursor)
			cursor.execute("SELECT * FROM %s" %self.table)
			return cursor.fetchall()
		connection.close()

#-----------------------#
# Main					#
#-----------------------#

# set global values (after declared objects)
url_table_object = url_table(database, 'urlTable', user, password)
form_table_object = form_table(database, 'formTable', user, password)

def main():

	start = time()

	depth = 0
	url_table_object.add_element([base_url], depth)
	crawl_url(base_url, depth)

	# warnings and errors will apprear here
	print

	try :
		print "== Crawled URLs == \n"
		print len(url_table_object.get_table_elements())
		#for element in url_table_object.get_table_elements() :
		#	print element
	except:
		print 'None'

	print

	try :
		print "== Found form fields == \n"
		print len(form_table_object.get_table_elements())
		#for element in form_table_object.get_table_elements() :
		#	print element
	except :
		print 'None'

	finish = time()

	total_time = finish - start
	print total_time

#-----------------------#
# Run Main				#
#-----------------------#

if __name__ == '__main__':
	main()
