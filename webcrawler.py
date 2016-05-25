#!/usr/bin/env python
def query1(keyword):
	import urllib
	import re
	query=urllib.urlopen("http://www.shopping.com/products?KW=<%s>"%keyword).read()
	result=query.find(keyword)
	return result
def query2(keyword,pageno):
	import urllib
	import re
	query=urllib.urlopen("http://www.shopping.com/products~PG-<%d>?KW=<%s>"%(int(pageno),keyword)).read()
	result=query.find(keyword)
	return result
