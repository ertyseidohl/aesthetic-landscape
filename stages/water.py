import random

import colors

WATER_COLOR = colors.LIGHT_BLUE

def water(img, seed_obj):
    (width, height) = img.size
    horizon = seed_obj['horizon']

    bg = list(img.getdata())

    bg = [WATER_COLOR if bg[i] == 255 else bg[i] for i in range(len(bg))]

    img.putdata(bg)

    return img



