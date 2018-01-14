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
    for i in range(2):
        x_l_e = x_cord
        y_l_e = y_cord

        while x_l_e >= 0:
            w = random.randint(5, 10)
            h = random.randint(-5, 5)
            x_l_s = x_l_e - w 
            y_l_s = y_l_e + h
            sep = random.randint(3,5)

            xy = ((x_l_s, y_l_s), (x_l_e, y_l_e))
            draw.line(xy, fill=DARK)
            (x_l_e, y_l_e) = (x_l_s, y_l_s)



def draw_rocks_right(draw, x_cord, y_cord):
    for i in range(2):
        x_l_s = x_cord
        y_l_s = y_cord

        while x_l_s <= 255:
            w = random.randint(5, 10)
            h = random.randint(-5, 5)
            x_l_e = x_l_s + w 
            y_l_e = y_l_s + h

            xy = ((x_l_s, y_l_s), (x_l_e, y_l_e))
            draw.line(xy, fill=DARK)
            (x_l_s, y_l_s) = (x_l_e, y_l_e)
