
# https://www.youtube.com/watch?v=NSbjuqHLxJA
# "thenewboston"

import os
from PIL import Image, ImageFilter
from DefaultItems import ImagesFolder

def main():
    sister_jpg = "Hillary.jpg"
    sister_file = os.path.join(ImagesFolder, sister_jpg)

    bucky_jpg = "balloon.png"
    bucky_file = os.path.join(ImagesFolder, bucky_jpg)

    sister = Image.open(sister_file)
    print("mode: ", sister.mode)
    r1, g1, b1 = sister.split()

    bucky = Image.open(bucky_file)
    print("mode: ", bucky.mode)
    r2, g2, b2, a2 = bucky.split()

    new_image = Image.merge("RGB", (r2, g1, b2))
    new_image.show()

    del sister
    del bucky
    del new_image
#    sister.save(sg)

if(__name__ == "__main__"):
    main()


