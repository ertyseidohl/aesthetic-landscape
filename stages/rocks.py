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
    (cx, cy) = (x_cord, y_cord)
    wb = random.randint(5, 10)
    wt = random.randint(5, 10)
    h = random.randint(3, 5)
    (ax, ay) = (cx - wt, cy)
    (bx, by) = (cx - wb, cy + h)
    draw.polygon([(ax, ay), (bx, by), (cx, cy)], fill=MIDDLE, outline=DARK)

    (dx, dy) = (cx, cy)
    while max(cx, dx) >= 0:
        wb = random.randint(5, 10)
        wt = random.randint(5, 10)
        hb = random.randint(-7, 7)
        ht = random.randint(-7, 7)
        (cx, cy) = (bx, by)
        (dx, dy) = (ax, ay)
        (bx, by) = (cx - wt, cy + ht)
        (ax, ay) = (dx - wb, dy + hb)
        draw.polygon([(ax, ay), (bx, by), (cx, cy), (dx, dy)], fill=MIDDLE, outline=DARK)


def draw_rocks_right(draw, x_cord, y_cord):
    xls = x_cord
    yls = y_cord

    while xls <= 255:
        w = random.randint(5, 10)
        h = random.randint(-5, 5)
        xle = xls + w 
        yle = yls + h

        xy = ((xls, yls), (xle, yle), ( (xle + xls)/2, yle - 5))
        draw.polygon(xy, fill=MIDDLE, outline=DARK)
        (xls, yls) = (xle, yle)
