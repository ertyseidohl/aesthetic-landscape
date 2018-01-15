from math import sqrt
import random
import reflection

import colors

WATER_COLOR = colors.BG_LIGHT
WATER_REFL_COLOR = colors.BG_LIGHTER
MOON_REFL_COLOR = colors.WHITE

def water(layers, layer_factory, seed_obj):

    mask = _get_water_mask(layers, seed_obj['width'], seed_obj['height'])

    fill_water_layer = layer_factory('water', reflection.NONE)
    fill_water_data = [WATER_COLOR if i else colors.TRANSPARENT for i in mask]
    fill_water_layer.img.putdata(fill_water_data)
    layers.append(fill_water_layer)

    moon_reflector = Reflector(
        _get_layer_by_name('moon', layers),
        layer_factory('moon_refl', reflection.IS_REFLECTION),
        seed_obj,
        mask,
        MOON_REFL_COLOR
    )
    moon_reflector.reflect_horizon(exclude_colors=[colors.BG_LIGHTEST])
    layers.append(moon_reflector.get_result_layer())

    mountain_reflector = Reflector(
        _get_layer_by_name('mountains', layers),
        layer_factory('mountains_refl', reflection.IS_REFLECTION),
        seed_obj,
        mask,
        WATER_REFL_COLOR
    )
    mountain_reflector.reflect_base()
    layers.append(mountain_reflector.get_result_layer())

    rocks1_reflector = Reflector(
        _get_layer_by_name('spit_1', layers),
        layer_factory('rocks_refl', reflection.IS_REFLECTION),
        seed_obj,
        mask,
        WATER_REFL_COLOR
    )
    rocks1_reflector.reflect_base()
    layers.append(rocks1_reflector.get_result_layer())

    rocks2_reflector = Reflector(
        _get_layer_by_name('spit_2', layers),
        layer_factory('rocks_refl', reflection.IS_REFLECTION),
        seed_obj,
        mask,
        WATER_REFL_COLOR
    )
    rocks2_reflector.reflect_base()
    layers.append(rocks2_reflector.get_result_layer())

    # water_lights_layer = layer_factory('water_lights', reflection.NONE)
    # _generate_water_lights(water_lights_layer, mask, seed_obj)
    # layers.append(water_lights_layer)

    return layers

def _get_water_mask(layers, width, height):
    mask = [True for i in range(width * height)]
    for layer in layers:
        if layer.reflection in (
            reflection.REFLECT_BASE,
            reflection.REFLECT_HORIZON,
            reflection.MASK
        ):
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

def _generate_water_lights(lights_layer, mask, seed_obj):
    width = seed_obj['width']
    height = seed_obj['height']
    horizon = seed_obj['horizon']
    lights_layer_data = [colors.TRANSPARENT for i in range(width * height)]

    # mid light streaks
    for y in range(horizon, height):
        if random.random() < 0.1:
            for x in range(random.randint(0, width // 3), random.randint(int(width*(2/3)), width)):
                if mask[y * width + x] and random.random() < 0.8:
                    lights_layer_data[y * width + x] = colors.WHITE

    lights_layer.img.putdata(lights_layer_data)



class Reflector:
    def __init__(self, orig_layer, refl_layer, seed_obj, mask, color):
        self.height = seed_obj['height']
        self.width = seed_obj['width']
        self.horizon = seed_obj['horizon']
        self.orig_layer = orig_layer
        self.refl_layer = refl_layer
        self.orig_data = list(orig_layer.img.getdata())
        self.refl_data = [colors.TRANSPARENT for i in range(self.width * self.height)]
        self.mask = mask
        self.color = color

    def reflect_base(self):
        for x in range(self.width):
            self._cast_ray(x, self.horizon)

    def reflect_horizon(self, exclude_colors = None):
        if not exclude_colors:
            exclude_colors = []
        exclude_colors += [colors.TRANSPARENT]
        for y_offset in range(self.height - self.horizon + 1):
            if y_offset % 2 == 0:
                orig_y = self.horizon - y_offset
                for x in range(self.width):
                    coord = (self.horizon + y_offset - 1) * self.width + x
                    orig_pixel = self.orig_data[orig_y * self.width + x]
                    if self.mask[coord] and orig_pixel not in exclude_colors:
                        self.refl_data[coord] = self.color

    def get_result_layer(self):
        self.refl_layer.img.putdata(self.refl_data)
        return self.refl_layer

    def _cast_ray(self, x, refl_point):
        y = refl_point
        while y < self.height:
            if self.orig_data[y * self.width + x] == colors.TRANSPARENT:
                y = self._cast_water(x, y)
            else:
                y = self._cast_land(x, y)

    def _cast_land(self, x, y):
        while y < self.height and self.orig_data[y * self.width + x] != colors.TRANSPARENT:
            y += 1
        return y

    def _cast_water(self, x, refl_point):
        y = refl_point
        while y < self.height and self.orig_data[y * self.width + x] == colors.TRANSPARENT:
            refl_y = refl_point + (refl_point - y) - 1
            if (self.orig_data[refl_y * self.width + x] == colors.TRANSPARENT):
                # if we have hit water again
                return y + 1
            if self.mask[y * self.width + x]:
                if y % 2 == 0:
                    self.refl_data[y * self.width + x] = self.color
                else:
                    self.refl_data[y * self.width + x] = WATER_COLOR
            y += 1
        return y
