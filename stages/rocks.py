import random
import os

from PIL import Image, ImageDraw

import colors
import reflection

MAX_ROCK_HEIGHT = 10
TOP_DECREASE_PERCENTAGE = 0.25
BOTTOM_DECREASE_PERCENTAGE = 0.05

def rocks(layers, layer_factory, seed_obj):
    random.seed(seed_obj['base_seed'])
    horizon = seed_obj['horizon']
    height = seed_obj['height']

    num_spits = random.randint(2, 5)

    y_mins = [random.randint(horizon - 10, height - 10) for i in range(num_spits)]
    y_mins.sort()
    y_mins.reverse()
    y_maxes = [y_min + random.randint(10, 30) for y_min in y_mins]

    rocks_layer = layer_factory('rocks', reflection.REFLECT_BASE)

    for i in range(num_spits):
        _draw_spit(rocks_layer, y_mins[i], y_maxes[i], seed_obj)

    return rocks_layer

def _draw_spit(layer, y_min, y_max, seed_obj, from_left=None, has_trees=None):
    height = seed_obj['height']
    width = seed_obj['width']
    horizon = seed_obj['horizon']

    y_max = min(y_max, height)

    spit_buffer = list(layer.img.getdata())

    has_trees = random.random() < 0.5 if has_trees == None else has_trees
    from_left = random.random() < 0.5 if from_left == None else from_left
    x = 0 if from_left else width - 1
    rock_height = random.randint(0, MAX_ROCK_HEIGHT)
    rock_height = 3
    rock_delta_height = 0
    while y_max > y_min and x >= 0 and x < width:
        for y in range(y_min - rock_height, y_max):
            coord = y * width + x

            if spit_buffer[coord] != colors.TRANSPARENT:
                continue

            elif y == y_max - 1 or (y_max - (y_min - rock_height) < 2):
                spit_buffer[coord] = colors.WHITE
            elif y == y_min and y < y_max - rock_height:
                spit_buffer[coord] = colors.FG_DARK
            elif y == y_max - 2:
                spit_buffer[coord] = colors.FG_DARK
            elif y == y_max - rock_height:
                spit_buffer[coord] = colors.FG_DARK
            elif y > y_max - rock_height:
                from_top = y - (y_max - rock_height)
                if from_left and from_top < 4 and rock_delta_height > 0:
                    spit_buffer[coord] = colors.FG_LIGHT
                elif not from_left and from_top < 4 and rock_delta_height < 0:
                    spit_buffer[coord] = colors.FG_LIGHT
                else:
                    spit_buffer[coord] = colors.FG_MID
            elif y > y_min:
                if (x + y) % 2 == 0 or random.random() < 0.2:
                    spit_buffer[coord] = colors.FG_DARK
                else:
                    spit_buffer[coord] = colors.FG_MID
        if random.random() < TOP_DECREASE_PERCENTAGE:
            y_min += 1
        if random.random() < BOTTOM_DECREASE_PERCENTAGE and y_max > horizon:
            y_max -= 1

        if rock_delta_height > 0 and random.random() < 0.8:
            rock_delta_height -= 1
        elif rock_delta_height == 0 and random.random() < 0.4:
            rock_delta_height -= 1
        elif rock_delta_height < 0 and random.random() < 0.3:
            rock_delta_height -= 1
        rock_height += rock_delta_height

        if rock_height < 1:
            if y_max - y_min > 5:
                rock_delta_height = random.randint(2, 3)
            else:
                 rock_height = 0

        if has_trees and random.random() < 0.15:
            _place_tree(spit_buffer, x, y_min, width)

        x += 1 if from_left else -1

    layer.img.putdata(spit_buffer)

def _place_tree(buf, x, y, width):
    tree_height = random.randint(4, 10)
    has_leaves = random.random() < 0.8

    for i in range(tree_height):
        coord = (y - i) * width + x
        if(coord > 0 and coord < len(buf)):
            buf[coord] = colors.FG_DARK
        if has_leaves and (i + x) % 2 == 0 and i < tree_height - 1:
            for leaf_x in range(min(-10 + i, 0), max(10 - i, 0) + 3):
                x_coord = x + leaf_x // 3
                if x_coord >= 0 and x_coord < width:
                    buf[(y - i) * width + x_coord] = colors.FG_DARK
