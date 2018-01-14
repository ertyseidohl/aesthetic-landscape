import random

COLOR_OFFSET = 0
MAX_COLORS = 8
DITHERS = ('none', 'a', 'b', 'c')

def background(img, palette, seed_obj):
	# random.seed(seed_obj['base_seed'])
	random.seed(0)

	# colors = random.randInt(0, MAX_COLORS)
	colors = 4
	# dither_pattern = DITHERS[random.randInt(0, len(DITHERS))]
	dither_pattern = DITHERS[0]

	bg = [i % colors for i in range(256 * 256)]

	# 0xe3, 0xba, 0xff
	# 0xff, 0xda, 0xf1

	for i in range(colors):
		palette.set_color(COLOR_OFFSET + i, (0xe3, 0xba, 0xff))

	img.putdata(bg)

	return (img, palette)
