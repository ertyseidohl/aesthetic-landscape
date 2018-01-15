from .background import background
from .mountains import mountains
from .rocks import rocks
from .water import water

def noop(layers, layer_factory, palette, seed):
	return ([], palette)

moon = noop
