'''
@author		Josh Gibbs & Louis Orleans
@website	http://0rleans.com/NightSkyLED
'''

import math, sys
from threading import Timer
from Patterns import Patterns
from LED import LED
from Helpers import States, LEDpattern
from Utils import Utils

class Controller (object):
	TIMERINTERVAL = 1

	def __init__ (self, LEDcount):
		self.LEDcount = LEDcount
		self.LEDs = []
		for i in xrange(LEDcount):
			self.LEDs.append(LED())
		self.patterns = Patterns(self.LEDs)

		self.timerFunc()

	def timerFunc (self):
		self.patterns.update()
		Timer(Controller.TIMERINTERVAL, self.timerFunc).start()

def main ():
	controller = Controller(50)

if __name__ == '__main__':
	main();