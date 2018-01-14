import random

from util import lerp

COLOR_OFFSET = 0
MAX_COLORS = 8
DITHERS = ('none', )

DARK = (0xe3, 0xba, 0xff)
LIGHT = (0xff, 0xda, 0xf1)

def background(img, palette, seed_obj):
	random.seed(seed_obj['base_seed'])

	num_colors = random.randint(4, MAX_COLORS)
	dither_pattern = random.choice(DITHERS)

	print(dither_pattern, num_colors)

	(width, height) = img.size

	bg = []

	if dither_pattern == 'none':
		total_pixels = width * height
		band_pixels = int(total_pixels / num_colors)
		for i in range(num_colors):
			bg += [i for x in range(band_pixels)]
		count = band_pixels * num_colors
		while count < total_pixels:
			bg += [num_colors - 1]
			count += 1

	img.putdata(bg)

	color_gen = lerp(DARK, LIGHT, num_colors)

	for i in range(num_colors):
		color = next(color_gen)
		palette.set_color(COLOR_OFFSET + i, color)

	return (img, palette)
