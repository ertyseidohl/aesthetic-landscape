import random

from PIL import ImageDraw

import colors
import reflection

COLOR_LIGHT = colors.WHITE
COLOR_CRATER = colors.BG_LIGHTEST

def moon(layers, layer_factory, seed_obj):
	random.seed(seed_obj['base_seed'])
	horizon = seed_obj['horizon']
	width = seed_obj['width']
	height = seed_obj['height']

	layer = layer_factory('moon', reflection.REFLECT_HORIZON)

	moon_x = random.triangular(0, width)
	# moon_y = random.triangular(0, horizon)
	moon_y = horizon
	moon_r = random.triangular(16, 64)

	draw = ImageDraw.Draw(layer.img)

	phase = random.choice((
		# _draw_new_moon,
		# _draw_crescent_moon,
		# _draw_gibbous_moon,
		_draw_full_moon,
	))

	phase(moon_x, moon_y, moon_r, draw, seed_obj)

	draw.rectangle(((0, seed_obj['horizon']), (seed_obj['width'], seed_obj['height'])), fill=colors.TRANSPARENT)

	return layer

def _generate_bounding_box(x, y, r):
	return ((x - r, y - r), (x + r, y + r))

def _draw_new_moon(x, y, r, draw, seed_obj):
	pass # lol

def _draw_crescent_moon(x, y,  r, draw, seed_obj):
	pass

def _draw_gibbous_moon(x, y, r, draw, seed_obj):
	pass

def _draw_full_moon(x, y, r, draw, seed_obj):
	draw.ellipse(_generate_bounding_box(x, y, r), COLOR_LIGHT)


	# crater_mask =
