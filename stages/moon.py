import random

from PIL import ImageDraw

import colors
import reflection

COLOR_LIGHT = colors.WHITE
COLOR_SHADOW = colors.BG_LIGHTEST

SQUASH_AMOUNT = 2

def moon(layers, layer_factory, seed_obj):
	random.seed(seed_obj['base_seed'])
	horizon = seed_obj['horizon']
	width = seed_obj['width']
	height = seed_obj['height']

	layer = layer_factory('moon', reflection.REFLECT_HORIZON)

	moon_r = int(random.triangular(8, 32))
	moon_x = int(random.triangular(0, width * 0.66 ))
	moon_y = int(random.triangular(moon_r, horizon))

	draw = ImageDraw.Draw(layer.img)

	phase = random.choice((
		_draw_crescent_moon,
		_draw_gibbous_moon,
		_draw_crescent_moon,
		_draw_gibbous_moon,
		_draw_crescent_moon,
		_draw_gibbous_moon,
	))

	phase(moon_x, moon_y, moon_r, draw, seed_obj)

	draw.rectangle(((0, seed_obj['horizon']), (seed_obj['width'], seed_obj['height'])), fill=colors.TRANSPARENT)

	return layer

def _draw_new_moon(x, y, r, draw, seed_obj):
	draw.ellipse(((x - r - SQUASH_AMOUNT, y - r), (x + r + SQUASH_AMOUNT, y + r)), COLOR_SHADOW)

def _draw_crescent_moon(x, y,  r, draw, seed_obj):
	draw.ellipse(((x - r - SQUASH_AMOUNT, y - r), (x + r + SQUASH_AMOUNT, y + r)), COLOR_SHADOW)

	draw.pieslice(
		((x - r, y - r + 1), (x + r, y + r - 1)),
		270,
		90,
		fill=COLOR_LIGHT
	)

	crescent_width = random.randint(0, r)

	draw.pieslice(
		((x - r + crescent_width, y - r + 1), (x + r - crescent_width, y + r - 1)),
		270,
		90,
		fill=COLOR_SHADOW
	)

def _draw_gibbous_moon(x, y, r, draw, seed_obj):
	#shadow
	draw.ellipse(((x - r - SQUASH_AMOUNT, y - r), (x + r + SQUASH_AMOUNT, y + r)), COLOR_SHADOW)
	# right
	draw.chord(
		((x - r, y - r + 1), (x + r, y + r - 1)),
		270,
		90,
		fill=COLOR_LIGHT
	)
	#left
	gibbous_shift = random.randint(0, r // 2)
	draw.chord(
		((x - r + gibbous_shift, y - r + 1), (x + r - gibbous_shift, y + r - 1)),
		90,
		270,
		fill=COLOR_LIGHT
	)
