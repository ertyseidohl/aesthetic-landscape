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

    def draw(self, draw, fill):
        draw.polygon(self.outline, fill=fill)
        for patch in self.patches:
            for pixel in patch:
                draw.point(pixel, fill=colors.WHITE)

    def outline_tail(self):
        return self.outline[len(self.outline) -1]

    def height(self):
        return max(self.outline[0][1] - self.peak[1], self.outline_tail()[1])

    def pixel_in_boundaries(self, x, y, exclusive=False):

        dx = 10000
        best = None
        for point in self.outline:
            deltax = abs(point[0] - x)
            if deltax < dx:
                best = point
                dx = deltax

        if exclusive:
            return best[1] < y < self.horizon
        return best[1] <= y <= self.horizon

    def add_patch(self, weight=None):

        if weight is None:
            start_pixel = self.peak
            weight = 0
        else:
            start_y = self.peak[1]
            start_y = start_y + (self.horizon - start_y) * random.triangular() * weight

            start_x = self.peak[0]
            while self.pixel_in_boundaries(start_x, start_y, exclusive=True):
                start_x = start_x - 1

            start_pixel = (start_x, start_y)

        width = random.randint(4, 8)
        max_length = math.ceil((self.horizon - self.peak[1]) / 2)
        patch = []

        top_offset = 0
        bottom_offset = random.randint(6 + math.ceil(10 * weight), 10 + math.ceil(10 * weight))
        for i in range(width):

            top_offset = top_offset + random.choice([2, 1, 1, 0, -1, -1, -2])
            bottom_offset = bottom_offset + random.choice([2, 1, 1, 0, -1, -1, -2])

            for j in range(top_offset, bottom_offset):
                x = start_pixel[0] + i - j
                y = start_pixel[1] + i + j

                if self.pixel_in_boundaries(x, y, exclusive=True):
                    patch.append((x,y))

        self.patches.append(patch)


def mountains(layers, layer_factory, seed_obj):
    random.seed(seed_obj['base_seed'])

    horizon = seed_obj['horizon']
    width = seed_obj['width']

    layer = layer_factory('mountains', reflection.REFLECT_BASE)
    img = layer.img

    num_peaks = random.randint(4, 40)
    mountain_ranges = [MountainRange(num_peaks=num_peaks, horizon=horizon, width=width)]
    draw = ImageDraw.Draw(img)

    for i, mountain_range in enumerate(mountain_ranges):
        for mountain in mountain_range.mountains:
            mountain.add_patch()
            for _ in range(random.randint(0, 3)):
                mountain.add_patch(random.random())

            mountain.draw(draw, random.choice((
                colors.FG_LIGHT,
            )))
    del draw

    return layer


SLOPES = [
    (0, 0),
    (2, 1),
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 3),
    (1, 2),
    (2, 1),
]


def _slope_start():
    slope_index = 0
    slope_stability = 0.
    slope_gravity = random.choice([0.1, 0.15, 0.15, 0.2, 0.25])
    return slope_index, slope_stability, slope_gravity


def _slope_stability(slope_index, slope_stability, slope_gravity):

    if slope_stability + random.random() > 1:
        slope_index = slope_index + random.choice([1, 1, 1, -1, -1, 2, -2])
        slope_stability = 0
    else:
        slope_stability += slope_gravity

    slope_index = max(slope_index, 0)
    slope_index = min(slope_index, len(SLOPES) -1)

    return slope_index, slope_stability

def _walk(mountain):

    mountain.outline = [mountain.peak]

    walk_xy = mountain.peak
    slope_index, slope_stability, slope_gravity = _slope_start()
    while walk_xy[1] <= mountain.horizon:
        slope_index, slope_stability = _slope_stability(slope_index, slope_stability, slope_gravity)
        walk_xy = (walk_xy[0] - SLOPES[slope_index][0], walk_xy[1] + SLOPES[slope_index][1])
        mountain.outline.append(walk_xy)

    walk_xy = mountain.peak
    slope_index, slope_stability, slope_gravity = _slope_start()
    while walk_xy[1] <= mountain.horizon:
        slope_index, slope_stability = _slope_stability(slope_index, slope_stability, slope_gravity)
        walk_xy = (walk_xy[0] + SLOPES[slope_index][0], walk_xy[1] + SLOPES[slope_index][1])
        mountain.outline.append(walk_xy)

    mountain.outline = sorted(mountain.outline, key=lambda x: x[0])

    return mountain
