import random
from PIL import Image, ImageDraw
import os
import colors

def rocks(layers, layer_factory, seed_obj):
    random.seed(seed_obj['base_seed'])

    layer = layer_factory('rocks')
    img = layer.img

    draw = ImageDraw.Draw(img)
    base_height = 10

    for i in range(random.randint(3, 5)):
        x_cord = random.randint(25, 225)
        y_cord = random.randint(125, 225)

        if x_cord < 125:
            draw_rocks_left(draw, x_cord, y_cord)
        else:
            draw_rocks_right(draw, x_cord, y_cord)

    return layer


def draw_rocks_left(draw, x_cord, y_cord):
    (top_coords, bot_coords) = ([(x_cord,y_cord)], [])
    heights = []

    (x, y) = (x_cord, y_cord)
    (x2, y2) = (x, y)
    i = 0
    j = 0
    while x >= 0:
        w = random.randint(2, 3)
        h = random.randint(-2, 2)
        (x, y) = (x - w, y + h)
        h = random.randint(6,10)
        if i%5 == 0:
            h = random.randint(3,6)
            j += 1
        heights.append(h)
        (x2, y2) = (x + random.randint(-1, 1), y - h - j)
        bot_coords.append((x, y))
        top_coords.append((x2, y2))
        i += 1

    bot_coords.reverse()
    coords = top_coords + bot_coords

    draw.polygon(coords, fill=colors.FG_MID, outline=colors.FG_DARK)
    bot_coords.reverse()
    for i in range(1, len(top_coords) - 1):
        if (i-1)%5 == 0 and i+5 < len(top_coords)-1:
            light_coords = [(x,y+1) for (x,y) in top_coords[i:i+5] ]

            (ax, ay) = light_coords[0]
            (bx, by) = light_coords[-1]
            end = [ (ax + bx)/2, (ay + by)/2 + (heights[i-5] + heights[i])/3]
            draw.polygon(light_coords + end, fill=colors.FG_LIGHT, outline=colors.FG_LIGHT)



def draw_rocks_right(draw, x_cord, y_cord):
    (top_coords, bot_coords) = ([(x_cord,y_cord)], [])
    heights = []

    (x, y) = (x_cord, y_cord)
    (x2, y2) = (x, y)
    i = 0
    j = 0
    while x <= 255:
        w = random.randint(2, 3)
        h = random.randint(-2, 2)
        (x, y) = (x + w, y + h)
        h = random.randint(6,10)
        if i%5 == 0:
            h = random.randint(3,6)
            j += 1
        heights.append(h)
        (x2, y2) = (x + random.randint(-1, 1), y - h - j)
        bot_coords.append((x, y))
        top_coords.append((x2, y2))
        i += 1

    bot_coords.reverse()
    coords = top_coords + bot_coords

    draw.polygon(coords, fill=colors.FG_MID, outline=colors.FG_DARK)
    bot_coords.reverse()
    for i in range(1, len(top_coords) - 1):
        if (i-1)%5 == 0 and i+6 < len(top_coords)-1:
            light_coords = [(x,y+1) for (x,y) in top_coords[i+1:i+6] ]

            (ax, ay) = light_coords[0]
            (bx, by) = light_coords[-1]
            end = [ (ax + bx)/2, (ay + by)/2 + (heights[i-5] + heights[i])/3]
            draw.polygon(light_coords + end, fill=colors.FG_LIGHT, outline=colors.FG_LIGHT)
