import random

from util import lerp

COLOR_OFFSET = 0
MAX_COLORS = 8
DITHERS = ('none', 'a', 'b', 'c')

def background(img, palette, seed_obj):
	# random.seed(seed_obj['base_seed'])
	random.seed(0)

	# num_colors = random.randInt(0, MAX_COLORS)
	num_colors = 8
	# dither_pattern = DITHERS[random.randInt(0, len(DITHERS))]
	dither_pattern = DITHERS[0]

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

	color_gen = lerp((0xe3, 0xba, 0xff), (0xff, 0xda, 0xf1), num_colors)

	for i in range(num_colors):
		color = next(color_gen)
		palette.set_color(COLOR_OFFSET + i, color)

	return (img, palette)
