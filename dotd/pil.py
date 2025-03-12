# PIL Python Image Library

from PIL import Image
import numpy as np

im = Image.open("sven.jpg")

print(im.format, im.size, im.mode)
# im.show()

gray = im.convert("L") # Luminance??
gray.show()

