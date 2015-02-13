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
			if percentDone >= 1:
				self.fromColor = self.toColor
			self.currentColor = HSL([self.fromColor.h + (self.fromColor.h - self.toColor) / percentDone.h, self.fromColor.s + (self.fromColor.s - self.toColor.s) / percentDone, self.fromColor.l + (self.fromColor.l - self.toColor.l) / percentDone])
			self.setColor(currentColor)

	def setColor (self, color, flashFade):
		# TODO: interface w/ uPayMeiFixIt's LED hardware interface
		return