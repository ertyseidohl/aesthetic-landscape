from PIL import Image, ImagePalette
import time
import colors
import random
import sys
import time

from PIL import Image, ImagePalette

from layer import layer_factory
from palettewrapper import PaletteWrapper
import stages

palette = PaletteWrapper()

# base_seed = random.randint(0, sys.maxsize)
base_seed = 512

random.seed(base_seed)

seed_object = {
    'base_seed': base_seed,
    'horizon': int(random.triangular(64, 192)),
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
    new_layers = func(layers, layer_factory, seed_object)
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

palette.set_colors(colors.COLOR_MAP)
image.putpalette(ImagePalette.ImagePalette('RGB', palette.serialize()))

image = image.resize((1024, 1024), resample=Image.NEAREST)

image.show()
image.save(f'img/motif_{int(time.time())}.png', 'PNG')
