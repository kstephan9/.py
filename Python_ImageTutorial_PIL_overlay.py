import os
from PIL import Image, ImageFilter
from DefaultItems import ImagesFolder

def main():
    sister_jpg = "Hillary.jpg"
    sister_file = os.path.join(ImagesFolder, sister_jpg)

    girl_png = "balloon.png"
    girl_file = os.path.join(ImagesFolder, girl_png)

   # print(girl)

    sister = Image.open(sister_file)
    girl = Image.open(girl_file)

    area = (100,100,190,227)
    sister.paste(girl, area)
    sister.show()

    sg = os.path.join(ImagesFolder,"sister_girl.png")

    sister.save(sg)


    del sister

    del girl
if(__name__ == "__main__"):
    main()


