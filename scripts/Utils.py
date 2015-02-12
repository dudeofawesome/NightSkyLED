import random

class Utils (object):
	@staticmethod
	def fillArrayRand (size, min, max):
		randArray = []
		for i in xrange(size):
			randArray.append(random.random() * (max - min) + min)
		return randArray