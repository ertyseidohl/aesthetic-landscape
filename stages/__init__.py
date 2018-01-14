from .background import background
from .mountains import mountains

def noop(img, palette, seed):
	return (img, palette)

rocks = noop
water = noop
moon = noop
