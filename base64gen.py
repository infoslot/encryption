import sys
import binascii

''' createGenerator() takes the binairy value(x) and the length of the chunks(l) as input 
	then the for loop walks through the binairy value with jump of value l instead of the normal 1 step
	yield return the value x from position i to position i + l.'''

def createGenerator(x,l):
	for i in xrange(0, len(x), l):
		yield x[i:i+l]

def main():
	total = len(sys.argv)
	if total < 2:
		print " "
		print "Usage: python base64gen.py <string to convert>"
		print " "
		exit(0)
	''' Take the commandline string as input'''
	s = sys.argv[1]

	''' create binairy representation of the input string '''
	''' binascii.hexlify convert the given string into in hex presentation, you can also use - string.encode('hex') '''
	x = bin(int(binascii.hexlify(s), 16))

	''' remove the first two positions (0b) '''
	x = x[2:]

	''' Check if the lengte of the binariy value is divisible by 6, otherwise add a zero '''
	if len(x) % 6 != 0:
		y = '0'
		x = y + x

	''' Generate the list, output is a list of chunks of x in which each part is 6 positions long'''
	w = list(createGenerator(x,6))
	reeks = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

	''' Walk throug every element of w, check if a element is divisible by 6, otherwise add zero'''
	p = ''
	for i in w:
		while len(i) % 6 != 0:
			i = i + '0'
		''' convert the binairy value to a decimal value and search the representational value in 'reeks'''
		u = int(i, 2)
		p = p + reeks[u]
	print p	

if __name__ == '__main__':
	main()

