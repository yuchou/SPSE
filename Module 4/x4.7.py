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

import sys

from bs4 import BeautifulSoup
import urllib

import MySQLdb as handler

#-----------------------#
# Variables				#
#-----------------------#

database = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
base_url = sys.argv[4]

MAX_DEPTH = sys.argv[5]

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

# craws a page and keeps going if max_depth not reached
def crawl_url(current_url, url_depth) :
	soup = get_soup(current_url)
	all_url = get_all_url(soup)
	all_forms = get_all_forms(soup)
	all_fields = get_all_fields(all_forms)
	# fill field table
	for field in all_fields :
		form_table_object.add_element(current_url, field)
	# keep crawling
	if url_depth < MAX_DEPTH :
		new_depth = url_depth+1
		for url in all_url :
			exists = url_table_object.url_exists(url)
			if not exists :
				url_table_object.add_element(url, new_depth)
				try :
					#thread = threading.Thread(target=crawl_url, args=(url,new_depth))
					#thread.start()
					#THREADS.append(thread)
					#thread.join()
					crawl_url(url,new_depth)
				except Exception, txt:
					pass

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

	def add_element(self, URL, depth) :
		try :
			connection = self.connect()
			with connection:
				cursor = connection.cursor()
				cursor.execute("CREATE TABLE IF NOT EXISTS %s(Id INT PRIMARY KEY AUTO_INCREMENT, URL VARCHAR(100), depth INT)" %self.table)
				cursor.execute("INSERT INTO %s(URL, depth) VALUES(\'%s\',\'%s\')" %(self.table,URL,depth))
		except Exception, txt :
			print 'Error : ',txt
		finally :
			connection.close()

	def get_table_elements(self) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor(handler.cursors.DictCursor)
			cursor.execute("SELECT * FROM %s" %self.table)
			return cursor.fetchall()
		connection.close()

	def url_exists(self, URL) :
		connection = self.connect()
		with connection:
			cursor = connection.cursor(handler.cursors.DictCursor)
			exists = cursor.execute("SELECT URL FROM %s WHERE URL=\'%s\'" %(self.table, URL))
		connection.close()
		return exists

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

	def add_element(self, url, field) :
		try :
			connection = self.connect()
			with connection:
				cursor = connection.cursor()
				cursor.execute("CREATE TABLE IF NOT EXISTS %s(Id INT PRIMARY KEY AUTO_INCREMENT, URL VARCHAR(100), field TEXT)" %self.table)
				cursor.execute("INSERT INTO %s(url, field) VALUES(\'%s\',\'%s\')" %(self.table,url,field))
		except Exception, txt :
			print 'Error : ',txt
		finally :
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

	depth = 0
	url_table_object.add_element(base_url, depth)
	crawl_url(base_url, depth)

	print

	try :
		print "Crawled URLs"
		for element in url_table_object.get_table_elements() :
			print element
	except:
		print 'None'

	print

	try :
		print "Found form fields"
		for element in form_table_object.get_table_elements() :
			print element
	except :
		print 'None'

#-----------------------#
# Run Main				#
#-----------------------#

if __name__ == '__main__':
	main()
