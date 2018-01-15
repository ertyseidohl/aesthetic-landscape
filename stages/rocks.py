import random
from PIL import Image, ImageDraw
import os


DARK = 9
MIDDLE = 10
LIGHT = 11

def rocks(img, palette, seed_obj):
    seed = os.urandom(1000)
    random.seed()
    palette.set_color(DARK, (0x33, 0xAF, 0xE0))
    palette.set_color(MIDDLE, (0x6C, 0xE0, 0xFF))
    palette.set_color(LIGHT, (0xBA, 0xF4, 0xFF))

    draw = ImageDraw.Draw(img)
    base_height = 10

    for i in range(random.randint(3, 5)):
        x_cord = random.randint(25, 225)
        y_cord = random.randint(125, 225)

        if x_cord < 125:
            draw_rocks_left(draw, x_cord, y_cord)
        else:
            draw_rocks_right(draw, x_cord, y_cord)

    return (img, palette)


def draw_rocks_left(draw, x_cord, y_cord):
    (top_coords, bot_coords) = ([(x_cord,y_cord)], [])
    heights = []

    (x, y) = (x_cord, y_cord)
    (x2, y2) = (x, y)
    i = 0
    while x >= 0:
        w = random.randint(5, 10)
        h = random.randint(-2, 2)
        (x, y) = (x - w, y + h)
        h = random.randint(3,10)
        heights.append(h)
        (x2, y2) = (x + random.randint(-1, 1), y - h - i)
        bot_coords.append((x, y))
        top_coords.append((x2, y2))
        i += 1

    bot_coords.reverse()
    coords = top_coords + bot_coords

    draw.polygon(coords, fill=MIDDLE, outline=DARK)
    bot_coords.reverse()
    for i in range(1, len(top_coords) - 1):
        (ax, ay) = top_coords[i]
        (bx, by) = top_coords[i+1]
        (cx, cy) = ( (ax + bx)/2, (ay + by)/2 + (heights[i-1] + heights[i])/3)
        draw.polygon([(ax, ay+1), (bx, by+1), (cx, cy)], fill=LIGHT, outline=LIGHT)



def draw_rocks_right(draw, x_cord, y_cord):
    (top_coords, bot_coords) = ([(x_cord,y_cord)], [])
    heights = []

    (x, y) = (x_cord, y_cord)
    (x2, y2) = (x, y)
    i = 0
    while x <= 255:
        w = random.randint(5, 10)
        h = random.randint(-5, 5)
        (x, y) = (x + w, y + h)
        h = random.randint(3,10)
        heights.append(h)
        (x2, y2) = (x + random.randint(-2, 2), y - h - i)
        bot_coords.append((x, y))
        top_coords.append((x2, y2))
        i += 1
    bot_coords.reverse()
    coords = top_coords + bot_coords

    draw.polygon(coords, fill=MIDDLE, outline=DARK)
    bot_coords.reverse()
    for i in range(1, len(top_coords) - 1):
        (ax, ay) = top_coords[i]
        (bx, by) = top_coords[i+1]
        (cx, cy) = ( (ax + bx)/2, (ay + by)/2 + (heights[i-1] + heights[i])/3)
        draw.polygon([(ax, ay+1), (bx, by+1), (cx, cy)], fill=LIGHT, outline=LIGHT)

