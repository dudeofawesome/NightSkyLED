from Helpers import HSL

class LED (object):
	def __init__ (self):
		self.fromColor = HSL(0, 0, 1)
		self.currentColor = HSL(0, 0, 1)
		self.toColor = HSL(0, 0, 1)
		self.interpolateTime = 5
		self.imterpolateStartTime = 0
	def update (self, pattern):
		if self.fromColor != self.toColor:
			# TODO: interpolation magic goes here
			percentDone = (calendar.timegm(time.gmtime()) - self.interpolateStartTime) / self.interpolateTime
			self.currentColor = self.fromColor + (self.fromColor - self.toColor) / percentDone

	def setColor (self, color, flashFade):
		# TODO: interface w/ uPayMeiFixIt's LED hardware interface
		return