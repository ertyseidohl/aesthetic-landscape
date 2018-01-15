from PIL import Image
import colors

IMAGE_SIZE = (256, 256)

class Layer:
    def __init__(self, name, reflective=True):
        self.reflective = reflective
        self.name = name
        self.img = Image.new('P', IMAGE_SIZE, color=colors.TRANSPARENT)

def layer_factory(name, reflective=True):
    return Layer(name, reflective=reflective)
