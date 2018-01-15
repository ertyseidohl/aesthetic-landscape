import random

WATER_COLOR_P = 20
# WATER_COLOR_RGB = (0xe3, 0xba, 0xff)
WATER_COLOR_RGB = [0xff, 0x66, 0x00]

def water(img, palette, seed_obj):
	(width, height) = img.size
	horizon = seed_obj['horizon']

	bg = list(img.getdata())

	for x in range(width):
		for y in range(height - horizon):
			_cast_ray(bg, x, horizon)

	img.putdata(bg)

	palette.set_color(WATER_COLOR_P, WATER_COLOR_RGB)

	palette.set_color(44, (0xff, 0x00, 0x66))

	return (img, palette)

def _cast_ray(bg, x, min_y):

