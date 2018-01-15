import random

WATER_COLOR_P = 20
WATER_COLOR_RGB = (0xe3, 0xba, 0xff)

def water(img, palette, seed_obj):
	(width, height) = img.size

	bg = list(img.getdata())

	for y in range(seed_obj['horizon'], height):
		for x in range(width):
			bg[(y * width) + x] = WATER_COLOR_P

	img.putdata(bg)

	palette.set_color(WATER_COLOR_P, WATER_COLOR_RGB)

	return (img, palette)


