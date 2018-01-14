import pytest

from motif.palette import PaletteWrapper

def test_set_color():
	palette = PaletteWrapper()

	palette.set_color(128, (3, 4, 5))

	print(palette.r)

	assert palette.get_color(128) == (3, 4, 5)

	# testing internals -- scaffolding test
	assert palette.r[128] == 3
	assert palette.g[128] == 4
	assert palette.b[128] == 5
