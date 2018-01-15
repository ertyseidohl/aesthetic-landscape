import random
from math import ceil
from util import lerp
import colors

PATTERNS = ('none', 'dither', 'diag')
COLORS = range(colors.DARK_PURPLE, colors.LIGHT_PURPLE)


def background(layers, layer_factory, seed_obj):

    layer = layer_factory('background')
    img = layer.img

    random.seed(seed_obj['base_seed'])

    num_colors = len(COLORS)
    pattern = random.choice(PATTERNS)

    bg = []

    width = img.size[0]
    height = seed_obj['horizon']

    if pattern == 'none':
        bg = _fill_bands(width, height, num_colors)
    if pattern == 'dither':
        bg = _fill_bands(width, height, num_colors)
        STAMP_SIZE = 12
        band_edges = [int(height / num_colors) * i for i in range(num_colors)][1:]
        stamp_pattern = [0 for i in range(0, random.randint(3, 10))] + [2 for i in range(0, random.randint(3, 6))]
        for edge in band_edges:
            for x in range(width):
                if x % 2 == 0:
                    for y_offset in range(STAMP_SIZE + stamp_pattern[(x // 2) % len(stamp_pattern)]):
                        if y_offset % 2 != 0:
                               swap(bg, width, x, edge + y_offset, x, edge - y_offset)
    if pattern == 'diag':
        BAND_WIDTH = random.randint(50, 150)
        band = [ceil(i / BAND_WIDTH) % num_colors for i in range(width)]
        for y in range(height):
            bg += [band[(i + y) % len(band)] for i in range(len(band))]

    img.putdata(bg)

    return layer

def swap(bg, width, x1, y1, x2, y2):
    bg[y1 * width + x1], bg[y2 * width + x2] = bg[y2 * width + x2], bg[y1 * width + x1]


def _fill_bands(width, height, num_colors):
    bg = []
    total_pixels = width * height
    band_pixels = int(total_pixels / num_colors)
    for i in COLORS:
        bg += [i for x in range(band_pixels)]
    count = band_pixels * num_colors
    while count < total_pixels:
        bg += [num_colors - 1]
        count += 1
    return bg
