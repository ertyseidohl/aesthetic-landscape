import random
from PIL import ImageDraw

random.seed(128)


def mountains(img, palette, seed_obj):

    mountain_range_count = random.randint(2, 4)
    mountain_ranges = [_build_range(random.randint(3, 5), 256, 100) for _ in range(mountain_range_count)]
    draw = ImageDraw.Draw(img)

    for mountain_range in mountain_ranges:
        for peaks in mountain_range:
            for i in range(len(peaks) - 1):
                draw.line([peaks[i], peaks[i+1]], fill=0)
    del draw

    return img, palette


def _build_range(peak_num, width, height):

    peak_xy_list = [(random.randint(0, width), random.randint(0, height)) for _ in range(peak_num)]
    peak_xy_list = sorted(peak_xy_list, key=lambda x: x[0])

    walks = [_walk(peak, height) for peak in peak_xy_list]
    return walks


def _walk(peak_xy, height):
    walk = [peak_xy]

    walk_xy = peak_xy
    while walk_xy[1] < height:
        walk_xy = (walk_xy[0] - random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        walk.append(walk_xy)

    walk_xy = peak_xy
    while walk_xy[1] < height:
        walk_xy = (walk_xy[0] + random.randint(1, 30), walk_xy[1] + random.randint(1, 30))
        walk.append(walk_xy)

    return sorted(walk, key=lambda x: x[0])