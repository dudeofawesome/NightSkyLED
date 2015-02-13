'''
@author		Josh Gibbs & Louis Orleans
@website	http://0rleans.com/NightSkyLED
'''

import math, sys, timeit
import Patterns
from Helpers import States, LEDpattern
from Utils import Utils

class Controller (object):
	def __init__ (self, LEDcount):
		self.LEDcount = LEDcount
		self.LEDs = []
		for i in xrange(LEDcount):
			self.LEDs.append(i)
		self.patterns = Patterns.Patterns(self.LEDs)

		t = timeit.Timer("self.patterns.update")
		# t.timeit(1)


def main ():
	controller = Controller(50)

if __name__ == '__main__':
	main();