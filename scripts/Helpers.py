from Utils import Utils

class LEDpattern (object):
	def __init__ (self, baseColors, chanceOfCommonRandomEvent, chanceOfRareRandomEvent, interpTime, noiseMasks):
		self.baseColors = baseColors
		self.chanceOfCommonRandomEvent = chanceOfCommonRandomEvent
		self.chanceOfRareRandomEvent = chanceOfRareRandomEvent
		self.interpTime = interpTime
		self.noiseMasks = noiseMasks

class TimeRange (object):
	def __init__ (self, _changeTo, _range):
		self.changeTo = _changeTo
		self.range = _range

class States (object):
	OFF = LEDpattern([[0, 1, 0]], 0, 0, 0, [])
	NIGHT = LEDpattern([[320, 0, 0.5]], 100, 0, 5, [])
	DAY = LEDpattern([[300, 0.3, 1]], 0, 0, 10, [])
	SUNRISE = LEDpattern([[140, 1, 0.7]], 0, 0, 20, [])
	SUNSET = LEDpattern([[125, 1, 0.8]], 0, 0, 20, [])
	RAIN = LEDpattern([[300, 0.1, 0.5]], 0, 0, 5, [])
	THUNDERSTORM = LEDpattern([[270, 0.1, 0.3], [180, 1, 1]], 0, 0, 5, [])
	ALARM = LEDpattern([[0, 1, 1]], 0, 0, 0, [])
	DISCO = LEDpattern([[0, 1, 1], [60, 1, 1], [120, 1, 1], [180, 1, 1], [240, 1, 1], [300, 1, 1]], 0, 0, 3, [])