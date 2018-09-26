import hashlib
import sys

class lut:
	def __init__(self, args): #hash can be derived from sys args if passed via commandline
		self.algo=args[0]
		self.combo=args[1].split(" ")

		self.hasher=hashlib.new(self.algo)

		self.charsets={
			"upper":['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
			"lower":['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
			"num":['0','1','2','3','4','5','6,','7','8','9']}
