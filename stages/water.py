import random

WATER_COLOR_P = 20
WATER_COLOR_RGB = (0xe3, 0xba, 0xff)

def water(img, palette, seed_obj):
	(width, height) = img.size
	horizon = seed_obj['horizon']

	bg = list(img.getdata())
	cast_result = bg[:]

	for x in range(width):
		_cast_ray(bg, cast_result, width, height, horizon, x, horizon)

	bg = [cast_result[i] if bg[i] == 255 else bg[i] for i in range(len(bg))]

	img.putdata(bg)

	palette.set_color(WATER_COLOR_P, WATER_COLOR_RGB)
	palette.set_color(44, (0xff, 0x00, 0x66))
	palette.set_color(55, (0xff, 0x66, 0x00))

	return (img, palette)

def _cast_ray(bg, cast_result, width, height, horizon, x, refl_point):
	y = refl_point
	while y < height:
		if bg[y * width + x] == 255:
			y = _cast_water(bg, cast_result, width, height, horizon, x, y)
		else:
			y = _cast_land(bg, cast_result, width, height, horizon, x, y)

def _cast_land(bg, cast_result, width, height, horizon, x, y):
	while y < height and bg[y * width + x] != 255:
		y += 1
	return y

def _cast_water(bg, cast_result, width, height, horizon, x, refl_point):
	y = refl_point
	while y < height and bg[y * width + x] == 255:
		refl_y = refl_point + (refl_point - y) - 1
		if (bg[refl_y * width + x] == 255):
			# if we have hit water again
			return y + 1

		if y % 2 == 0:
			cast_result[y * width + x] = bg[refl_y * width + x]
		else:
			cast_result[y * width + x] = WATER_COLOR_P

		y += 1
	return y




