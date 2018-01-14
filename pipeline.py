#import x

pil_object = {}
seed_object = {}

funcs = []


def register_function(func):
    funcs.append(func)

# register_function(x.add_background)

for func in funcs:
    pil_object = func(pil_object, seed_object)
