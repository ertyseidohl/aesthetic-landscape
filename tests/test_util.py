from motif.util import lerp

def test_lerp():
	color_1 = (0, 0, 0)
	color_2 = (4, 4, 4)
	steps = 4

	gen = lerp(color_1, color_2, steps)

	assert(next(gen) == (0.0, 0.0, 0.0))
	assert(next(gen) == (1.0, 1.0, 1.0))
	assert(next(gen) == (2.0, 2.0, 2.0))
	assert(next(gen) == (3.0, 3.0, 3.0))
