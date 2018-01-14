import random

WATER_COLOR_P = 20
WATER_COLOR_RGB = (0xe3, 0xba, 0xff)

def water(img, palette, seed_obj):
	width = img.size[0]
	height = img.size[1] - seed_obj['horizon']

	offset = seed_obj['horizon'] * width

	existing = img.getdata()

	existing = [existing if i < offset else WATER_COLOR_P for i in range(width * height)]

	palette.set_color(WATER_COLOR_P, WATER_COLOR_RGB)

	return (img, palette)


