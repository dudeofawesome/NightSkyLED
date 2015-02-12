import math, sys, datetime, random
from Helpers import LEDpattern, TimeRange, States

class Patterns (object):
	def __init__ (self, LEDs):
		self.LEDs = LEDs
		self.state = States.OFF
		self.chanceOfRareRandomEvent = 1000000000
		self.chanceOfCommonRandomEvent = 100
		self.transitionStateTime = 30
		self.timeRanges = [TimeRange(States.NIGHT, [19, 5]), TimeRange(States.SUNRISE, [5, 5.30]), TimeRange(States.DAY, [5.30, 18.30]), TimeRange(States.SUNSET, [18.30, 19]), TimeRange(States.ALARM, [9, 9.10])]

	def update (self):
		timeAsDouble = datetime.datetime.hour + (datetime.datetime.minute / 100)
		for timeRange in self.timeRanges:
			# TODO: make this work for over night ranges (eg: [23, 01])
			if (timeAsDouble >= timeRange.range[0] and timeAsDouble <= timeRange.range[1]):
				# TODO: make transitions soft
				self.state = timeRange.changeTo
				for i in xrange(len(self.LEDs)):
					self.LEDs[i].toColor = noiseMasks[0][i]
		for i in xrange(len(self.LEDs)):
			if (random.random() * self.chanceOfCommonRandomEvent == 0):
				self.LEDs[i].toColor = noiseMasks[0][i]

	def setState (self, newState):
		self.state = newState