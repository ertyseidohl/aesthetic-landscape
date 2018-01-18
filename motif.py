import base64
import colors
from io import BytesIO
import random
import sys
import time

from PIL import Image, ImagePalette

from layer import layer_factory, IMAGE_SIZE
from palettewrapper import PaletteWrapper
import stages
import reflection

def motif(seed=None, is_webapp=False):
    seed = str(seed) if seed else str(random.randint(0, sys.maxsize))
    random.seed(seed)
    palette = PaletteWrapper()

    seed_object = {
        'base_seed': seed,
        'horizon': int(random.triangular(IMAGE_SIZE[0] * 0.4, IMAGE_SIZE[0] * 0.8)),
        'height': IMAGE_SIZE[0],
        'width': IMAGE_SIZE[1],
    }

    funcs = [
        stages.background,
        stages.moon,
        stages.mountains,
        stages.rocks,
        stages.water
    ]

    layers = []
    for func in funcs:
        new_layers = func(layers, layer_factory, seed_object)
        if type(new_layers) == list:
            layers = layers + new_layers
        else:
            layers.append(new_layers)

    image = layer_factory('base', reflection.NONE).img
    for layer in layers:
        layer_img_data = list(layer.img.getdata())
        image_data = image.getdata()

        image_data = [image_data[i] if layer_img_data[i] == colors.TRANSPARENT else layer_img_data[i] for i in range(len(image_data))]
        image.putdata(image_data)

    palette.set_colors(colors.generate_palette(seed_object))
    image.putpalette(ImagePalette.ImagePalette('RGB', palette.serialize()))

    image = image.resize((IMAGE_SIZE[0] * 4, IMAGE_SIZE[1] * 4), resample=Image.NEAREST)

    if is_webapp:
        buffer = BytesIO()
        image.save(buffer, format='PNG')
        return (seed, base64.b64encode(buffer.getvalue()))
    else:
        image.show()
        image.save(f'img/motif_{int(time.time())}.png', 'PNG')

    print(f'Seed: {seed}')

if __name__ == '__main__':
    motif()
