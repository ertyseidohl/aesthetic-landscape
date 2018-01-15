from PIL import Image
import colors

IMAGE_SIZE = (150, 150)

class Layer:
    def __init__(self, name, reflection):
        self.reflection = reflection
        self.name = name
        self.img = Image.new('P', IMAGE_SIZE, color=colors.TRANSPARENT)

def layer_factory(name, reflection):
    return Layer(name, reflection)
