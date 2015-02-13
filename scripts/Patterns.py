import math, sys, datetime, random
from Helpers import LEDpattern, TimeRange, States
from Utils import Utils

class Patterns (object):
	def __init__ (self, LEDs):
		self.LEDs = LEDs
		self.state = States.OFF
		self.transitionStateTime = 30
		self.LEDcount = len(LEDs)
		States.OFF.noiseMasks = []
		States.NIGHT.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		States.DAY.noiseMasks = []
		States.SUNRISE.noiseMasks = []
		States.SUNSET.noiseMasks = []
		States.RAIN.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		States.THUNDERSTORM.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		States.ALARM.noiseMasks = []
		States.DISCO.noiseMasks = []
		self.timeRanges = [TimeRange(States.NIGHT, [19, 5]), TimeRange(States.SUNRISE, [5, 5.30]), TimeRange(States.DAY, [5.30, 18.30]), TimeRange(States.SUNSET, [18.30, 19]), TimeRange(States.ALARM, [9, 9.10])]

	def update (self):
		# Check if in a new time range
		timeAsDouble = datetime.datetime.hour + (datetime.datetime.minute / 100)
		for timeRange in self.timeRanges:
			# TODO: make this work for over night ranges (eg: [23, 01])
			if (timeAsDouble >= timeRange.range[0] and timeAsDouble <= timeRange.range[1]):
				self.state = timeRange.changeTo
				for i in xrange(len(self.LEDs)):
					self.LEDs[i].toColor = self.state.baseColors[math.floor(random.random() * len(self.state.baseColors))][i]
		for i in xrange(len(self.LEDs)):
			if (self.state.chanceOfCommonRandomEvent != 0 and random.random() * self.state.chanceOfCommonRandomEvent == 0):
				self.LEDs[i].toColor = self.state.commonRandomEventColors[math.floor(random.random() * len(self.state.commonRandomEventColors))][i]
			if (self.state.chanceOfRareRandomEvent != 0 and random.random() * self.state.chanceOfRareRandomEvent == 0):
				self.LEDs[i].toColor = self.state.rareRandomEventColors[math.floor(random.random() * len(self.state.rareRandomEventColors))][i]
			# Apply noise mask, if any
			if len(self.state.noiseMasks) > 0:
				self.LEDs[i].toColor *= self.state.noiseMasks[math.floor(random.random() * len(self.state.noiseMasks))][i]
			self.LEDs[i].upate()

	def setState (self, newState):
		self.state = newState