
# https://www.youtube.com/watch?v=NSbjuqHLxJA
# "thenewboston"

import os
from PIL import Image, ImageFilter
from DefaultItems import ImagesFolder

def main():
    sister_jpg = "Hillary.jpg"
    sister_file = os.path.join(ImagesFolder, sister_jpg)

    sister = Image.open(sister_file)
    print("mode: ", sister.mode)
    r, g, b = sister.split()

    r.show()

    new_image = Image.merge("RGB", (r, g, b))
    new_image.show()
#    sister.save(sg)


    del sister

if(__name__ == "__main__"):
    main()


