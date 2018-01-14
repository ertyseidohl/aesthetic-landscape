from .background import background
from .mountains import mountains
from .rocks import rocks
from .water import water

def noop(img, palette, seed):
	return (img, palette)

moon = noop
