from .background import background
from .mountains import mountains
from .rocks import rocks

def noop(img, palette, seed):
	return (img, palette)

water = noop
moon = noop
