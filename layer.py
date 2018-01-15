from PIL import Image

IMAGE_SIZE = (256, 256)

class Layer:
    def __init__(self, name, reflective=True):
        self.name = name
        self.img = Image.new('P', IMAGE_SIZE, color=255)

def layer_factory(name, reflective=True):
    return Layer(name, reflective=reflective)
