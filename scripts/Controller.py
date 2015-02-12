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
		States.OFF = LEDpattern([[0, 1, 0]], 0, 0, 0, [0])
		States.NIGHT = LEDpattern([[320, 0, 0.5]], 100, 0, 5, [Utils.fillArrayRand(LEDcount, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1)])
		States.DAY = LEDpattern([[300, 0.3, 1]], 0, 0, 10, [0])
		States.SUNRISE = LEDpattern([[140, 1, 0.7]], 0, 0, 20, [0])
		States.SUNSET = LEDpattern([[125, 1, 0.8]], 0, 0, 20, [0])
		States.RAIN = LEDpattern([[300, 0.1, 0.5]], 0, 0, 5, [Utils.fillArrayRand(LEDcount, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1)])
		States.THUNDERSTORM = LEDpattern([[270, 0.1, 0.3], [180, 1, 1]], 0, 0, 5, [Utils.fillArrayRand(LEDcount, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1), Utils.fillArrayRand(LEDcount - 1, 0, 1)])
		States.ALARM = LEDpattern([[0, 1, 1]], 0, 0, 0, [0])
		States.DISCO = LEDpattern([[0, 1, 1], [60, 1, 1], [120, 1, 1], [180, 1, 1], [240, 1, 1], [300, 1, 1]], 0, 0, 3, [0])

		t = timeit.Timer("self.patterns.update")
		# t.timeit(1)


def main ():
	controller = Controller(50)

if __name__ == '__main__':
	main();