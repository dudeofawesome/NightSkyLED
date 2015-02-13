from Utils import Utils

class LEDpattern (object):
	def __init__ (self, baseColors, commonRandomEventColors, rareRandomEventColors, chanceOfCommonRandomEvent, chanceOfRareRandomEvent, interpTime, noiseMasks):
		self.baseColors = baseColors
		self.commonRandomEventColors = commonRandomEventColors
		self.rareRandomEventColors = rareRandomEventColors
		self.chanceOfCommonRandomEvent = chanceOfCommonRandomEvent
		self.chanceOfRareRandomEvent = chanceOfRareRandomEvent
		self.interpTime = interpTime
		self.noiseMasks = noiseMasks

class TimeRange (object):
	def __init__ (self, _changeTo, _range):
		self.changeTo = _changeTo
		self.range = _range

class HSL(object):
	def __init__ (self, hsl):
		if isinstance(hsl, list):
			self.h = 0 if hsl[0] is None else hsl[0]
			self.s = 0.5 if hsl[1] is None else hsl[1]
			self.l = 0 if hsl[2] is None else hsl[2]
	def toRGB ():
		if s == 0.0:
			return [self.l, self.l, self.l]
		i = int(self.h * 6.0) # XXX assume int() truncates!
		f = (self.h * 6.0) - i
		p = self.l * (1.0 - self.s)
		q = self.l * (1.0 - self.s * f)
		t = self.l * (1.0 - self.s * (1.0 - f))
		i = i % 6
		if i == 0:
			return [v, t, p]
		if i == 1:
			return [q, v, p]
		if i == 2:
			return [p, v, t]
		if i == 3:
			return [p, q, v]
		if i == 4:
			return [t, p, v]
		if i == 5:
			return [v, p, q]
	def __add__ (self, right):
		if isinstance(right, list):
			return [self.h + right.h, self.s + right.s, self.l + right.l]
		else:
			return [self.h + right, self.s + right, self.l + right]
	def __sub__ (self, right):
		if isinstance(right, list):
			return [self.h - right.h, self.s - right.s, self.l - right.l]
		else:
			return [self.h - right, self.s - right, self.l - right]
	def __mul__ (self, right):
		if isinstance(right, list):
			return [self.h * right.h, self.s * right.s, self.l * right.l]
		else:
			return [self.h * right, self.s * right, self.l * right]
	def __truediv__ (self, right):
		if isinstance(right, list):
			return [self.h / right.h, self.s / right.s, self.l / right.l]
		else:
			return [self.h / right, self.s / right, self.l / right]
	def __floordiv__ (self, right):
		if isinstance(right, list):
			return [self.h / right.h, self.s / right.s, self.l / right.l]
		else:
			return [self.h / right, self.s / right, self.l / right]
	def __str__(self):
		return "HSL(%s, %s, %s)" % (self.h, self.s, self.l)

class States (object):
	OFF = LEDpattern([HSL([0, 1, 0])], [], [], 0, 0, 0, [])
	NIGHT = LEDpattern([HSL([264, 0, 0.2])], [HSL([0, 0, 0.4])], [HSL([60, 1, .72])], 0, 100000, 5, [])
	DAY = LEDpattern([HSL([205, 1, 0.7])], [], [], 0, 0, 10, [])
	SUNRISE = LEDpattern([HSL([13, 1, 0.6]), HSL([193, 1, 0.81])], [], [], 0, 0, 20, [])
	SUNSET = LEDpattern([HSL([13, 1, 0.6]), HSL([273, 1, 0.7])], [], [], 0, 0, 20, [])
	RAIN = LEDpattern([HSL([226, 0.58, 0.48]), HSL([226, 0.66, 0.76])], [], [], 0, 0, 5, [])
	THUNDERSTORM = LEDpattern([HSL([270, 0.1, 0.3])], [HSL([180, 1, 1])], [], 100, 0, 5, [])
	ALARM = LEDpattern([HSL([0, 1, 0.5])], [], [], 0, 0, 0, [])
	DISCO = LEDpattern([HSL([0, 1, 0.5]), HSL([30, 1, 0.5]), HSL([60, 1, 0.5]), HSL([90, 1, 0.5]), HSL([120, 1, 0.5]), HSL([150, 1, 0.5]), HSL([180, 1, 0.5]), HSL([210, 1, 0.5]), HSL([240, 1, 0.5]), HSL([270, 1, 0.5]), HSL([300, 1, 0.5]), HSL([330, 1, 0.5])], [], [], 0, 0, 3, [])