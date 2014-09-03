import sys
import binascii

'''
	callable by example:
	from base64gen import *

	x = Base64gen()
	x.goconvert(string)
'''

class Base64gen:
	count = 0

	def __init__(self):
		print ""
	
	def createGenerator(self,x,l):
		for i in xrange(0, len(x), l):
			yield x[i:i+l]

	def goconvert(self,s):
		self.s = s
		x = bin(int(binascii.hexlify(s), 16))
		x = x[2:]
		if len(x) % 6 != 0:
			y = '0'
			x = y + x
		w = list(self.createGenerator(x,6))
		reeks = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
		p = ''
		for i in w:
			while len(i) % 6 != 0:
				i = i + '0'
			u = int(i, 2)
			p = p + reeks[u]
		print p	


