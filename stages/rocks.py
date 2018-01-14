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
    height = 10
    width = height*1.5
    x = x_cord
    y = y_cord
    while x + width >= 0:
        xy = ((x, y), (x+width, y+height))
        draw.line(xy, fill=DARK)
        x = x - width


def draw_rocks_right(draw, x_cord, y_cord):
    height = 10
    width = height*1.5
    x = x_cord
    y = y_cord
    while x <= 255:
        xy = ((x, y), (x+width, y+height))
        draw.line(xy, fill=DARK)
        x = x + width
