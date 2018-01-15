import math
import random

from PIL import ImageDraw

import colors
import reflection

class MountainRange:

    def __init__(self, num_peaks, horizon, width):
        self.horizon = horizon
        self.num_peaks = num_peaks
        self.width = width

        bandwidth_factor = random.triangular()
        yshift_factor = random.random() - 0.5
        mid = (horizon / 2)
        yshift = mid * yshift_factor
        band_middle = mid + yshift

        top_height = int(max(band_middle - (mid * bandwidth_factor), 20))
        bottom_height = int(min(band_middle + (mid * bandwidth_factor), horizon - horizon / 10))

        peak_xy_list = [(random.randint(0, width), random.randint(top_height, bottom_height)) for _ in range(num_peaks)]
        peak_xy_list = sorted(peak_xy_list, key=lambda x: x[0])

        self.mountains = [Mountain(peak, self.horizon) for peak in peak_xy_list]


class Mountain:

    def __init__(self, peak, horizon):
        self.outline = []
        self.peak = peak
        self.horizon = horizon
        self.patches = []
        _walk(self)

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


def mountains(layers, layer_factory, seed_obj):
    random.seed(seed_obj['base_seed'])

    horizon = seed_obj['horizon']
    width = seed_obj['width']

    layer = layer_factory('mountains', reflection.REFLECT_BASE)
    img = layer.img

    num_peaks = random.randint(4, 7)
    mountain_ranges = [MountainRange(num_peaks=num_peaks, horizon=horizon, width=width)]
    draw = ImageDraw.Draw(img)

    for i, mountain_range in enumerate(mountain_ranges):
        for mountain in mountain_range.mountains:
            # if random.choices([False, False, False, False, True]):
            #     mountain.add_patch(random.random())
            mountain.draw(draw, random.choice((
                colors.FG_LIGHT,
                colors.FG_MID,
                colors.FG_DARK,
            )))
    del draw

    return layer

SLOPES = [
    (0, 0),
    (4, 1),
    (3, 1),
    (2, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4)
]


def _slope_start():
    slope_index = 0
    slope_stability = 0.
    return slope_index, slope_stability


def _slope_stability(slope_index, slope_stability):

    if slope_stability + random.random() > 1.25:
        slope_index = slope_index + random.choice([1, 1, 1, -1, 2, -2])
        slope_stability = 0
    else:
        slope_stability += 0.1

    slope_index = max(slope_index, 0)
    slope_index = min(slope_index, len(SLOPES) -1)

    return slope_index, slope_stability

def _walk(mountain):

    mountain.outline = [mountain.peak]

    walk_xy = mountain.peak
    slope_index, slope_stability = _slope_start()
    while walk_xy[1] <= mountain.horizon:
        slope_index, slope_stability = _slope_stability(slope_index, slope_stability)
        walk_xy = (walk_xy[0] - SLOPES[slope_index][0], walk_xy[1] + SLOPES[slope_index][1])
        mountain.outline.append(walk_xy)

    walk_xy = mountain.peak
    slope_index, slope_stability = _slope_start()
    while walk_xy[1] <= mountain.horizon:
        slope_index, slope_stability = _slope_stability(slope_index, slope_stability)
        walk_xy = (walk_xy[0] + SLOPES[slope_index][0], walk_xy[1] + SLOPES[slope_index][1])
        mountain.outline.append(walk_xy)

    mountain.outline = sorted(mountain.outline, key=lambda x: x[0])

    return mountain
