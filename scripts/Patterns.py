import math, sys, datetime, random
from datetime import datetime
from Helpers import LEDpattern, TimeRange, States, HSL
from Utils import Utils

class Patterns (object):
	def __init__ (self, LEDs):
		self.LEDs = LEDs
		self.state = States.OFF
		self.transitionStateTime = 30
		self.LEDcount = len(LEDs)


		States.OFF = LEDpattern([HSL([0, 1, 0])], [], [], 0, 0, 0, [])
		States.NIGHT = LEDpattern([HSL([264, 0, 0.2])], [HSL([0, 0, 0.4])], [HSL([60, 1, .72])], 0, 100000, 5, [])
		States.DAY = LEDpattern([HSL([205, 1, 0.7])], [], [], 0, 0, 10, [])
		States.SUNRISE = LEDpattern([HSL([13, 1, 0.6]), HSL([193, 1, 0.81])], [], [], 0, 0, 20, [])
		States.SUNSET = LEDpattern([HSL([13, 1, 0.6]), HSL([273, 1, 0.7])], [], [], 0, 0, 20, [])
		States.RAIN = LEDpattern([HSL([226, 0.58, 0.48]), HSL([226, 0.66, 0.76])], [], [], 0, 0, 5, [])
		States.THUNDERSTORM = LEDpattern([HSL([270, 0.1, 0.3])], [HSL([180, 1, 1])], [], 100, 0, 5, [])
		States.ALARM = LEDpattern([HSL([0, 1, 0.5])], [], [], 0, 0, 0, [])
		States.DISCO = LEDpattern([HSL([0, 1, 0.5]), HSL([30, 1, 0.5]), HSL([60, 1, 0.5]), HSL([90, 1, 0.5]), HSL([120, 1, 0.5]), HSL([150, 1, 0.5]), HSL([180, 1, 0.5]), HSL([210, 1, 0.5]), HSL([240, 1, 0.5]), HSL([270, 1, 0.5]), HSL([300, 1, 0.5]), HSL([330, 1, 0.5])], [], [], 0, 0, 3, [])

		print "HSL(226, 0.58, 0.48) == " + str(HSL([226, 0.58, 0.48]))

		# States.OFF.noiseMasks = []
		# States.NIGHT.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		# States.DAY.noiseMasks = []
		# States.SUNRISE.noiseMasks = []
		# States.SUNSET.noiseMasks = []
		# States.RAIN.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		# States.THUNDERSTORM.noiseMasks = [Utils.fillArrayRand(self.LEDcount, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5), Utils.fillArrayRand(self.LEDcount - 1, 0.5, 1.5)]
		# States.ALARM.noiseMasks = []
		# States.DISCO.noiseMasks = []

		self.timeRanges = [TimeRange(States.NIGHT, [19, 5]), TimeRange(States.SUNRISE, [5, 5.30]), TimeRange(States.DAY, [5.30, 18.30]), TimeRange(States.SUNSET, [18.30, 19]), TimeRange(States.ALARM, [9, 9.10])]

	def update (self):
		# Check if in a new time range
		timeAsDouble = datetime.now().hour + (datetime.now().minute / 100)
		for timeRange in self.timeRanges:
			# TODO: make this work for over night ranges (eg: [23, 01])
			if timeRange.range[0] - timeRange.range[1] < 0:
				if (self.state != timeRange.changeTo and timeAsDouble >= timeRange.range[0] and timeAsDouble <= timeRange.range[1]):
					print "Applying state"
					self.state = timeRange.changeTo
					for i in xrange(len(self.LEDs)):
						self.LEDs[i].toColor = self.state.baseColors[int(math.floor(random.random() * len(self.state.baseColors)))]
					break
			else:
				if (self.state != timeRange.changeTo and timeAsDouble <= timeRange.range[0] and timeAsDouble >= timeRange.range[1]):
					print "Applying state"
					self.state = timeRange.changeTo
					for i in xrange(len(self.LEDs)):
						self.LEDs[i].toColor = self.state.baseColors[int(math.floor(random.random() * len(self.state.baseColors)))]
					break

		for i in xrange(len(self.LEDs)):
			if (self.state.chanceOfCommonRandomEvent != 0 and random.random() * self.state.chanceOfCommonRandomEvent == 0):
				self.LEDs[i].toColor = self.state.commonRandomEventColors[int(math.floor(random.random() * len(self.state.commonRandomEventColors)))]
			if (self.state.chanceOfRareRandomEvent != 0 and random.random() * self.state.chanceOfRareRandomEvent == 0):
				self.LEDs[i].toColor = self.state.rareRandomEventColors[int(math.floor(random.random() * len(self.state.rareRandomEventColors)))]
			# Apply noise mask, if any
			# if len(self.state.noiseMasks) > 0:
			# 	self.LEDs[i].toColor *= self.state.noiseMasks[int(math.floor(random.random() * len(self.state.noiseMasks)))][i]
			self.LEDs[i].update()

	def setState (self, newState):
		self.state = newState