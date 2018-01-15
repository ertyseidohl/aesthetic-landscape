from util import lerp

WHITE = 0
DARK_BLUE = 1
LIGHT_BLUE = 4
DARK_PURPLE = 5
LIGHT_PURPLE = 8
TRANSPARENT = 255

DARK_BLUE_RGB = (0x33, 0xAF, 0xE0)
LIGHT_BLUE_RGB = (0xBA, 0xF4, 0xFF)
DARK_PURPLE_RGB = (0xE3, 0xBA, 0xFF)
LIGHT_PURPLE_RGB = (0xFF, 0xDA, 0xF1)
WHITE_RGB = (0xFF, 0xFF, 0xFF)
TRANSPARENT_RGB = (0xFF, 0x00, 0xFF)

# color map for palette
COLOR_MAP = [(0, 0, 0) for i in range(256)]

COLOR_MAP[0] = WHITE_RGB

_blue_lerp = lerp(DARK_BLUE_RGB, LIGHT_BLUE_RGB, 3)
COLOR_MAP[1] = next(_blue_lerp)
COLOR_MAP[2] = next(_blue_lerp)
COLOR_MAP[3] = next(_blue_lerp)
COLOR_MAP[4] = next(_blue_lerp)

_purp_lerp = lerp(DARK_PURPLE_RGB, LIGHT_PURPLE_RGB, 3)
COLOR_MAP[5] = next(_purp_lerp)
COLOR_MAP[6] = next(_purp_lerp)
COLOR_MAP[7] = next(_purp_lerp)
COLOR_MAP[8] = next(_purp_lerp)

COLOR_MAP[255] = TRANSPARENT_RGB



