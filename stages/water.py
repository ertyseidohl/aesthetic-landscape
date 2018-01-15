import random

WATER_COLOR_P = 20
# WATER_COLOR_RGB = (0xe3, 0xba, 0xff)
WATER_COLOR_RGB = [0xff, 0x66, 0x00]

def water(img, palette, seed_obj):
	(width, height) = img.size
	horizon = seed_obj['horizon']

	bg = list(img.getdata())

	for y in range(horizon, height):
		refl_y = horizon + (horizon - y) - 1
		is_reflected = refl_y > 0
		for x in range(width):
			coord = (y * width) + x
			if bg[coord] == 255:
				if is_reflected:
					color = bg[(refl_y * width) + x]
					bg[coord] = 44
				else:
					bg[coord] = WATER_COLOR_P

	img.putdata(bg)

	palette.set_color(WATER_COLOR_P, WATER_COLOR_RGB)

	palette.set_color(44, (0xff, 0x00, 0x66))

	return (img, palette)


