class PaletteWrapper:
	def __init__(self):
		self.r = [i for i in range(256)]
		self.g = [i for i in range(256)]
		self.b = [i for i in range(256)]

	def set_color(self, eight_bit, rgb):
		assert type(eight_bit) is int and eight_bit > 0 and eight_bit < 256
		assert type(rgb) is list or type(rgb) is tuple and len(rgb) is 3

		self.r[eight_bit] = rgb[0]
		self.g[eight_bit] = rgb[1]
		self.b[eight_bit] = rgb[2]

	def get_color(self, eight_bit):
		return (
			self.r[eight_bit],
			self.g[eight_bit],
			self.b[eight_bit])

	def serialize(self):
		return [r for r in self.r] + [g for g in self.g] + [b for b in self.b]
