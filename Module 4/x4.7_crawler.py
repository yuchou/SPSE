#!/usr/bin/python

print "                 __                      "
print "                |__|____ ___  __         "
print "                |  \__  \\\\  \/ /       "
print "                |  |/ __ \\\\   /        "
print "            /\__|  (____  /\_/           "
print "            \______|    \/               "
print "                                         "

print	'Module 4'
print	'Attacking Web Applications'
print

import threading

from bs4 import BeautifulSoup
import urllib

MAX_DEPTH = 1

base_url = 'http://miguelharth-bedoya.com/'
base_url = 'http://umbo.tk'
base_url = 'http://newegg.com'
base_url = 'http://ebay.com'

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
	if url_depth < MAX_DEPTH :
		new_depth = url_depth+1
		for url in all_url :
			try :
				thread = threading.Thread(target=crawl_url, args=(url,new_depth))
				thread.start()
				thread.join()
			except Exception, txt:
				pass

depth = 0
crawl_url(base_url, depth)




