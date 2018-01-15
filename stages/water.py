from math import sqrt
import random

import colors

WATER_COLOR = colors.BG_LIGHTER

def water(layers, layer_factory, seed_obj):

    mask = _get_water_mask(layers, seed_obj['width'], seed_obj['height'])

    layer = layer_factory('water')

    # _reflect_horizon('moon')
    layers.append(
        _reflect_horizon(
            mask,
            _get_layer_by_name('background', layers),
            layer_factory('background_refl'),
            seed_obj
        )
    )
    # _reflect_base('mountains', seed_obj)
    # _reflect_base('rocks', seed_obj)

    return layers

def _get_water_mask(layers, width, height):
    mask = [True for i in range(width * height)]
    for layer in layers:
        if layer.reflective:
            orig_data = list(layer.img.getdata())
            for i in range(len(orig_data)):
                if orig_data[i] != colors.TRANSPARENT:
                    mask[i] = False

    return mask

def _get_layer_by_name(name, layers):
    for layer in layers:
        if layer.name == name:
            return layer
    raise ValueError(f'No layer with name {name}')

def _reflect_horizon(mask, orig_layer, refl_layer, seed_obj):
    horizon = seed_obj['horizon']
    height = seed_obj['height']
    width = seed_obj['width']

    orig_data = list(orig_layer.img.getdata())
    refl_data = [colors.TRANSPARENT for i in range(width * height)]

    for y_offset in range(height - horizon + 1):
        orig_y = horizon - int(y_offset ** 0.75)
        for x in range(width):
            coord = (horizon + y_offset - 1) * width + x
            if mask[coord]:
                refl_data[coord] = orig_data[orig_y * width + x]

    refl_layer.img.putdata(refl_data)

    return refl_layer
