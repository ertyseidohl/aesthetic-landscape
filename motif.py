from PIL import Image
import stages

img = Image.new('RGB', (256, 256), color=(255, 255, 255))

img = img.resize((1024, 1024), resample=Image.NEAREST)

pil_object = {}
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
    pil_object = func(pil_object, seed_object)

img.show()
