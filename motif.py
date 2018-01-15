import random
import sys
import time

from PIL import Image, ImagePalette

from layer import layer_factory
from palette import PaletteWrapper
import stages

palette = PaletteWrapper()

# base_seed = random.randint(0, sys.maxsize)
base_seed = 512

random.seed(base_seed)

seed_object = {
    'base_seed': base_seed,
    'horizon': int(random.triangular(64, 192)),
    'colors': []
}

funcs = []

def register_function(func):
    funcs.append(func)

register_function(stages.background)
register_function(stages.mountains)
register_function(stages.rocks)
register_function(stages.moon)
register_function(stages.water)

layers = []
for func in funcs:
    new_layers, palette = func(layers, layer_factory, palette, seed_object)
    if type(new_layers) == list:
        layers = layers + new_layers
    else:
        layers.append(new_layers)

image = layer_factory('base').img
for layer in layers:
    layer_img_data = list(layer.img.getdata())
    image_data = image.getdata()

    image_data = [image_data[i] if layer_img_data[i] == 255 else layer_img_data[i] for i in range(len(image_data))]
    image.putdata(image_data)

palette.set_color(255, (0xff, 0x00, 0x00))
image.putpalette(ImagePalette.ImagePalette('RGB', palette.serialize()))

image = image.resize((1024, 1024), resample=Image.NEAREST)

image.show()
image.save(f'img/motif_{int(time.time())}.png', 'PNG')
