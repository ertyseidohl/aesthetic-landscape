from PIL import Image

img = Image.new('RGB', (256, 256), color=(255, 255, 255))

img = img.resize((1024, 1024), resample=Image.NEAREST)

img.show()
