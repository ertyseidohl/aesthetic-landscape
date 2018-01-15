import math
from PIL import ImageDraw
import random

from util import lerp

COLOR_OFFSET = 30

LIGHT = (0xBA, 0xF4, 0xFF)
DARK = (0x33, 0xAF, 0xE0)

class Mountain:

    def __init__(self):
        self.outline = []
        self.peak = ()
        self.patches = []

    def draw(self, draw,fill):
        draw.polygon(self.outline, fill=fill)
        for patch in self.patches:

            for i, row in enumerate(patch):
                for j, tup in enumerate(row):
                    if tup and tup[2]:
                        draw.point((tup[0], tup[1]), fill=fill-1)

    def outline_tail(self):
        return self.outline[len(self.outline) -1]

    def height(self):
        return max(self.outline[0][1] - self.peak[1], self.outline_tail()[1])

    def add_patch(self, weight):

        width = 20
        height = 20
        patch = [[0 for _ in range(width)] for _ in range(height)]

        origin_x = self.peak[0] + 5
        origin_y = self.peak[1] + 50

        for j in range(height):
            start_x = 0
            start_y = j

            offset_bottom = math.ceil((random.triangular() * width) / 2)
            offset_top = width - math.ceil((random.triangular() * width) / 2)

            i = 0
            while start_y >= 0 and start_x >= 0:
                if i > offset_bottom and i < offset_top:
                    patch[start_y][start_x] = (origin_x + start_x, origin_y + start_y, 1)
                else:
                    patch[start_y][start_x] = (origin_x + start_x, origin_y + start_y, 0)

                i += 1
                start_y = start_y - 1
                start_x = start_x + 1
        self.patches.append(patch)

    def shift_y(self, amount):
        self.outline = [(xy[0], xy[1] + amount) for xy in self.outline]


def mountains(img, palette, seed_obj):
    random.seed(seed_obj['base_seed'])

    mountain_range_count = random.randint(2, 4)
    mountain_ranges = [_build_range(random.randint(3, 5), 256, 100) for _ in range(mountain_range_count)]
    draw = ImageDraw.Draw(img)

    for i, mountain_range in enumerate(mountain_ranges):
        for mountain in mountain_range:
            if random.choices([False, False, False, False, True]):
                mountain.add_patch(random.random())
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

    walk_xy = mountain.peak
    while walk_xy[1] <= height:
        walk_xy = (walk_xy[0] - random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        mountain.outline.append(walk_xy)

    walk_xy = mountain.peak
    while walk_xy[1] <= height:
        walk_xy = (walk_xy[0] + random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        mountain.outline.append(walk_xy)

    mountain.outline = sorted(mountain.outline, key=lambda x: x[0])

    return mountain
