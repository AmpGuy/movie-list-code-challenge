'''
	Module: unitest
	Purpose: Test REST API for movie_script.py
	Date: 11/08/2015
	Author: T. Bellavia
'''
import unittest
import urllib2
import urllib
import sys

base_url = 'http://127.0.0.1:8080/api/movies/'
get_name = 'Resident%20Evil'
get_unknown_name = 'No%20Evil'
post_exist_movie = ['Resident%20Evil:%20Extinction','2000','Fox']
post_new_movie_no_prod = ['Stripes','1983','']
put_exist_movie = ['Resident%20Evil','2015','Fox']
put_nonexist_movie = ['Barney','2015','Fox']
delete_exist_movie = ['Resident%20Evil:%20Apocalypse','2006','Film Gems']
delete_nonexist_movie = ['Chuckie','2012','studio']

class TestRestAPIMethods(unittest.TestCase):

	def test_GET(self):
		sys.stdout.write('\n\ntest_GET\n==================\n')
		url = base_url + get_name
		sys.stdout.write('\n\nURL: %s\n' % url)
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_GET_Unknown_Movie(self):
		sys.stdout.write('\n\ntest_GET_Unknown_Movie\n==================\n')
		url = base_url + get_unknown_name
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_PUT(self):
		sys.stdout.write('\n\ntest_PUT\n==================\n')
		url = base_url + put_nonexist_movie[0]
		data = urllib.urlencode([('released=' + put_nonexist_movie[1], 'production=' + put_nonexist_movie[2])])
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req, data)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_PUT_Unknown_Movie(self):
		sys.stdout.write('\n\ntest_PUT_Unknown_Movie\n==================\n')
		url = base_url + put_exist_movie[0]
		data = urllib.urlencode([('released=' + put_exist_movie[1], 'production=' + put_exist_movie[2])])
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req, data)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)


	def test_DELETE_Exist(self):
		sys.stdout.write('\n\ntest_DELETE_Exist\n==================\n')
		url = base_url + delete_exist_movie[0]
		sys.stdout.write('\n\nURL: %s\n' % url)
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_DELETE_NonExist(self):
		sys.stdout.write('\n\ntest_DELETE_NonExist\n==================\n')
		url = base_url + delete_nonexist_movie[0]
		sys.stdout.write('\n\nURL: %s\n' % url)
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_POST_NonExist(self):
		sys.stdout.write('\n\ntest_POST_NonExist\n==================\n')
		data = urllib.urlencode([('released=' + post_new_movie_no_prod[1], 'production=' + post_new_movie_no_prod[2])])
		url = base_url + post_new_movie_no_prod[0]
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req, data)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

	def test_POST_Exist(self):
		sys.stdout.write('\n\ntest_POST_Exist\n==================\n')
		data = urllib.urlencode([('released=' + post_exist_movie[1], 'production=' + post_exist_movie[2])])
		sys.stdout.write('\n'+ data +'\n')
		url = base_url + post_exist_movie[0]
		req = urllib2.Request(url)
		fd = urllib2.urlopen(req, data)
		while 1:
			data = fd.read(1024)
			if not len(data):
				break
			sys.stdout.write(data)

if __name__ == '__main__':
    unittest.main()
