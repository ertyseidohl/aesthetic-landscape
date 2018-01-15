from motif.util import lerp

def test_lerp():
    color_1 = (0, 0, 0)
    color_2 = (4, 4, 4)
    steps = 5

    gen = lerp(color_1, color_2, steps)

    assert(next(gen) == (0, 0, 0))
    assert(next(gen) == (1, 1, 1))
    assert(next(gen) == (2, 2, 2))
    assert(next(gen) == (3, 3, 3))
    assert(next(gen) == (4, 4, 4))
