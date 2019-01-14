#!/usr/bin/python3

from PIL import Image
from getpath import getpath
import os

path = getpath('../set/pic')

size = (1920, 1080)

fl = os.listdir(path)

for name in fl:
    im = Image.open(os.path.join(path, name))

    bx = size[0] // 2 - im.size[0] // 2
    by = size[1] // 2 - im.size[1] // 2
    ex = size[0] // 2 + im.size[0] // 2
    ey = size[1] // 2 + im.size[1] // 2

    p = Image.new('RGBA', size, (255, 255, 255))
    p.paste(im, (bx, by))
    p.save(os.path.join(path, name), format="png")
    print(name + ": Done.")
