class LED (object):
	def __init__ (self):
		self.fromColor = [0, 0, 1]
		self.toColor = [0, 0, 1]
		self.interpolateTime = 5
		self.percentInterp = 1
		self.setColor (self, color, flashFade):
			# TODO: interface w/ uPayMeiFixIt's LED hardware interface
			return