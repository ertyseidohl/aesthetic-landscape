from PIL import Image, ImagePalette
import stages
from palette import PaletteWrapper

img = Image.new('P', (256, 256), color=255)

palette = PaletteWrapper()

seed_object = {}

funcs = []

def register_function(func):
    funcs.append(func)

register_function(stages.background)
register_function(stages.mountains)
register_function(stages.rocks)
register_function(stages.water)
register_function(stages.moon)

for func in funcs:
    img, palette = func(img, palette, seed_object)

print(len(palette.serialize()))

img.putpalette = ImagePalette.ImagePalette('RGB', palette.serialize())

img = img.resize((1024, 1024), resample=Image.NEAREST)

img.show()
