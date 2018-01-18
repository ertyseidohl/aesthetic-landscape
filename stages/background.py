import random
from math import ceil
from util import lerp
import colors
import reflection

PATTERNS = ('none', 'dither', 'diag')
COLORS = range(colors.BG_DARKEST, colors.BG_LIGHTEST)


def background(layers, layer_factory, seed_obj):
    random.seed(seed_obj['base_seed'])

    layer = layer_factory('background', reflection.MASK)
    img = layer.img

    num_colors = len(COLORS)
    # pattern = random.choice(PATTERNS)
    pattern = 'dither'

    bg = []

    width = seed_obj['width']
    height = seed_obj['height']
    horizon = seed_obj['horizon']

    if pattern == 'none':
        bg = _fill_bands(width, horizon, num_colors)
    if pattern == 'dither':
        bg = _fill_bands(width, horizon, num_colors)
        STAMP_SIZE = int(random.triangular(2, horizon // num_colors))
        band_edges = [int(horizon / num_colors) * i for i in range(num_colors)][1:]
        stamp_pattern = [0 for i in range(0, random.randint(3, 10))] + [2 for i in range(0, random.randint(3, 6))]
        for edge in band_edges:
            for x in range(width):
                if x % 2 == 0:
                    for y_offset in range(STAMP_SIZE + stamp_pattern[(x // 2) % len(stamp_pattern)]):
                        if y_offset % 2 != 0:
                            swap(bg, width, x, edge + y_offset, x, edge - y_offset)
    if pattern == 'diag':
        BAND_WIDTH = random.randint(50, 100)
        band = [ceil(i / BAND_WIDTH) % num_colors for i in range(width)]
        band[0] = band[1] # fix 0th index
        for y in range(horizon):
            bg += [COLORS[band[(i + y) % len(band)]] for i in range(len(band))]

    _fill_stars(bg, width, horizon)

    img.putdata(bg)

    return layer

def swap(bg, width, x1, y1, x2, y2):
    bg[y1 * width + x1], bg[y2 * width + x2] = bg[y2 * width + x2], bg[y1 * width + x1]


def _fill_bands(width, horizon, num_colors):
    bg = []
    total_pixels = width * horizon
    band_height = int(horizon / num_colors)
    for i in COLORS:
        bg += [i for x in range(band_height * width)]
    count = band_height * width * num_colors
    while count < total_pixels:
        bg += [COLORS[num_colors - 1]]
        count += 1
    return bg


def _fill_stars(bg, width, horizon):

    def random_index():
        if random.choices([True, False]):
            return random.randint(0, (width * horizon) - 1)
        else:
            return random.randint(0, ((width * horizon) / 2)-1)

    # small stars
    for _ in range(random.randint(10, 30)):
        bg[random_index()] = colors.WHITE

    # big stars
    for _ in range(random.randint(5, 10)):
        index = random_index()
        bg[index] = colors.WHITE
        if index - 1 >= 0:
            bg[index - 1] = colors.WHITE

        if index + 1 < width * horizon:
            bg[index + 1] = colors.WHITE

        if index - width >= 0:
            bg[index - width] = colors.WHITE

        if index + width < width * horizon:
            bg[index + width] = colors.WHITE
