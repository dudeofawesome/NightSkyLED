import math, sys, datetime, random
from Helpers import LEDpattern, TimeRange, States
from Utils import Utils

class Patterns (object):
	def __init__ (self, LEDs):
		self.LEDs = LEDs
		self.state = States.OFF
		self.transitionStateTime = 30
		self.timeRanges = [TimeRange(States.NIGHT, [19, 5]), TimeRange(States.SUNRISE, [5, 5.30]), TimeRange(States.DAY, [5.30, 18.30]), TimeRange(States.SUNSET, [18.30, 19]), TimeRange(States.ALARM, [9, 9.10])]
		self.LEDcount = len(LEDs)
		States.OFF = LEDpattern([[0, 1, 0]], 0, 0, 0, [0])
		States.NIGHT = LEDpattern([[320, 0, 0.5]], 100, 0, 5, [Utils.fillArrayRand(self.LEDcount, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1)])
		States.DAY = LEDpattern([[300, 0.3, 1]], 0, 0, 10, [0])
		States.SUNRISE = LEDpattern([[140, 1, 0.7]], 0, 0, 20, [0])
		States.SUNSET = LEDpattern([[125, 1, 0.8]], 0, 0, 20, [0])
		States.RAIN = LEDpattern([[300, 0.1, 0.5]], 0, 0, 5, [Utils.fillArrayRand(self.LEDcount, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1)])
		States.THUNDERSTORM = LEDpattern([[270, 0.1, 0.3], [180, 1, 1]], 0, 0, 5, [Utils.fillArrayRand(self.LEDcount, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1), Utils.fillArrayRand(self.LEDcount - 1, 0, 1)])
		States.ALARM = LEDpattern([[0, 1, 1]], 0, 0, 0, [0])
		States.DISCO = LEDpattern([[0, 1, 1], [60, 1, 1], [120, 1, 1], [180, 1, 1], [240, 1, 1], [300, 1, 1]], 0, 0, 3, [0])

	def update (self):
		timeAsDouble = datetime.datetime.hour + (datetime.datetime.minute / 100)
		for timeRange in self.timeRanges:
			# TODO: make this work for over night ranges (eg: [23, 01])
			if (timeAsDouble >= timeRange.range[0] and timeAsDouble <= timeRange.range[1]):
				# TODO: make transitions soft
				self.state = timeRange.changeTo
				for i in xrange(len(self.LEDs)):
					self.LEDs[i].toColor = self.state.noiseMasks[math.floor(random.random() * len(self.state.noiseMasks))][i]
		for i in xrange(len(self.LEDs)):
			if (self.state.chanceOfCommonRandomEvent != 0 and random.random() * self.state.chanceOfCommonRandomEvent == 0):
				self.LEDs[i].toColor = self.state.baseColors[math.floor(random.random() * len(self.state.baseColors))][i]
			if (self.state.chanceOfRareRandomEvent != 0 and random.random() * self.state.chanceOfRareRandomEvent == 0):
				self.LEDs[i].toColor = self.state.baseColors[math.floor(random.random() * len(self.state.baseColors))][i]
		for LED in self.LEDs:
			LED.upate()

	def setState (self, newState):
		self.state = newState