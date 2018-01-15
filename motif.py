from PIL import Image, ImagePalette
import stages
import time
from palette import PaletteWrapper
import random
import sys

img = Image.new('P', (256, 256), color=255)

palette = PaletteWrapper()

# base_seed = random.randint(0, sys.maxsize)
base_seed = 512

random.seed(base_seed)

seed_object = {
    'base_seed': base_seed,
    'horizon': int(random.triangular(64, 192))
    'colors': [

    ]
}

funcs = []

def register_function(func):
    funcs.append(func)

register_function(stages.background)
register_function(stages.mountains)
register_function(stages.rocks)
register_function(stages.moon)
register_function(stages.water)

for func in funcs:
    img, palette = func(img, palette, seed_object)

palette.set_color(255, (0xff, 0x00, 0x00))
img.putpalette(ImagePalette.ImagePalette('RGB', palette.serialize()))

img = img.resize((1024, 1024), resample=Image.NEAREST)

img.show()
img.save(f'img/motif_{int(time.time())}.png', 'PNG')
