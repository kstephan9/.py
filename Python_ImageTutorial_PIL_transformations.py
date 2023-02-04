
# https://www.youtube.com/watch?v=El0mbC7olFc
# "thenewboston"

import os
from PIL import Image, ImageFilter, ImageFilter
from DefaultItems import ImagesFolder

def main():
    bucky_jpg = "Hillary.jpg"
    bucky_file = os.path.join(ImagesFolder, bucky_jpg)

    bucky = Image.open(bucky_file)
    bucky.show()

    black_white = bucky.convert("L")
    black_white.show()
    detail = bucky.filter(ImageFilter.DETAIL)
    detail.show()

    del bucky
#    sister.save(sg)

if(__name__ == "__main__"):
    main()


