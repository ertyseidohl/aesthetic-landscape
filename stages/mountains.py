import random
from PIL import ImageDraw

from util import lerp

COLOR_OFFSET = 30

LIGHT = (0xBA, 0xF4, 0xFF)
DARK = (0x33, 0xAF, 0xE0)

class Mountain:

    def __init__(self):
        self.outline = []

    def draw(self, draw,fill):
        draw.polygon(self.outline, fill=fill)

    def shift_y(self, amount):
        self.outline = [(xy[0], xy[1] + amount) for xy in self.outline]


def mountains(img, palette, seed_obj):
    random.seed(seed_obj['base_seed'])

    mountain_range_count = random.randint(2, 4)
    mountain_ranges = [_build_range(random.randint(3, 5), 256, 100) for _ in range(mountain_range_count)]
    draw = ImageDraw.Draw(img)

    for i, mountain_range in enumerate(mountain_ranges):
        for mountain in mountain_range:
            mountain.shift_y(i * 100)
            mountain.draw(draw, i + COLOR_OFFSET)
    del draw

    color_gen = lerp(LIGHT, DARK, mountain_range_count)
    for i in range(mountain_range_count):
        palette.set_color(i + COLOR_OFFSET, next(color_gen))

    return img, palette


def _build_range(peak_num, width, height):

    peak_xy_list = [(random.randint(0, width), random.randint(0, height)) for _ in range(peak_num)]
    peak_xy_list = sorted(peak_xy_list, key=lambda x: x[0])

    mountain_range = [_walk(peak, height) for peak in peak_xy_list]
    return mountain_range


def _walk(peak_xy, height):

    mountain = Mountain()
    mountain.peak = peak_xy
    mountain.outline = [peak_xy]
    mountain.patches = []

    walk_xy = mountain.peak
    while walk_xy[1] <= height:
        walk_xy = (walk_xy[0] - random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        mountain.outline.append(walk_xy)

        if random.randint(0, 10) > 5:
            walk_index = len(mountain.outline) - 1

            x_shift = walk_index * 2 + random.randint(0, 2)

            start = mountain.outline[walk_index][0] + x_shift, mountain.outline[walk_index][1]
            end = mountain.outline[walk_index - 1][0] + x_shift, mountain.outline[walk_index -1][1]
            mountain.patches.append((start, end))

    walk_xy = mountain.peak
    while walk_xy[1] <= height:
        walk_xy = (walk_xy[0] + random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        mountain.outline.append(walk_xy)

    mountain.outline = sorted(mountain.outline, key=lambda x: x[0])

    return mountain
