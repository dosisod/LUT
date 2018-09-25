import hashlib
import sys

class lut:
	def __init__(self, args): #hash can be derived from sys args if passed via commandline
		self.algo=args[0]
		self.combo=args[1].split(" ")

		self.hasher=hashlib.new(self.algo)
