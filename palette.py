class PaletteWrapper:
	def __init__(self):
		self.r = [i for i in range(256)]
		self.g = [i for i in range(256)]
		self.b = [i for i in range(256)]

	def serialize(self):
		return [r for r in self.r] + [g for g in self.g] + [b for b in self.b]
