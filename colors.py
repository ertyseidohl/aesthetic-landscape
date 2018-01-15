from util import lerp
import random

WHITE = 0
WHITE_RGB = (0xff, 0xff, 0xff)

BG_DARKEST = 1
BG_DARKER = 2
BG_DARK = 3
BG_LIGHT = 4
BG_LIGHTER = 5
BG_LIGHTEST = 6
FG_DARK = 7
FG_MID = 8
FG_LIGHT = 9

TRANSPARENT = 10
TRANSPARENT_RGB = (0xff, 0x00, 0xff)

_purples = (
    (0x0b, 0x00, 0x84),
    (0x53, 0x09, 0xd3),
    (0x95, 0x5f, 0xf3),
)

_pinks = (
    (0xe3, 0xba, 0xff),
    (0xed, 0xd2, 0xff),
    (0xff, 0xda, 0xf1),
)

_teals = (
    (0x33, 0xaf, 0xe0),
    (0x48, 0xd6, 0xff),
    (0x93, 0xed, 0xff),
)

_oranges = (
    (0xdc, 0x2a, 0x5a),
    (0xff, 0x5c, 0x66),
    (0xff, 0xd9, 0xa6),
)

_yellows = (
    (0xff, 0xeb, 0xc7),
    (0xff, 0xb4, 0xbb),
    (0xff, 0x9b, 0xb8),
)

def generate_palette(seed_obj):
    random.seed(seed_obj['base_seed'])

    choices = (
        _yellows,
        _oranges,
        _pinks,
        _purples,
        _teals,
    )

    bg_choice = random.choice(choices)

    bg_lerp = lerp(bg_choice[2], bg_choice[0], 6)
    fg_base = random.choice(choices)

    color_map = [
        WHITE_RGB, # 0
        next(bg_lerp), # 1
        next(bg_lerp), # 2
        next(bg_lerp), # 3
        next(bg_lerp), # 4
        next(bg_lerp), # 5
        next(bg_lerp), # 6
        fg_base[0], # 7
        fg_base[1], # 8
        fg_base[2], # 9
        TRANSPARENT_RGB, #10
    ]

    return color_map

