asdfas

import os
import re


from PIL import Image, ImageFilter
from shutil import copy
from DefaultItems import ImagesTestFolder as ITF
from DefaultItems import PhotosFolder as Source

#ITF_png = ITF + "\\" + "png"
#print(ITF_png)

#ITF_300 = ITF + "\\" + "300"
#print(ITF_300)

#ITF_1200 = ITF + "\\" + "1200"
#print(ITF_1200)

ITF_1024 = ITF + "\\" + "1024"
print(ITF_1024)

ITF_768 = ITF + "\\" + "768"
print(ITF_768)

def main():

    #
    # cycle over all files in folder 'Source'
    #

    for f in os.listdir(Source):
        if os.path.isdir(os.path.join(Source,f)):
            print(os.path.join(Source,f) , "is a folder")
        else:
            fn, fext = os.path.splitext(f)
            pattern = re.compile(r'Nora')
            matches = pattern.finditer(f)
            for match in matches:
                source_full_name = os.path.join(Source,f)

    #            if os.path.isfile(os.path.join(ITF + '/' + fn + '.png')):
                #print("test: ", f, os.path.join(ITF,f))
                if os.path.isfile(os.path.join(ITF,f)):
                    # file already exists there.
                    pass
                else:
                    print("did not exist", f)
                    newPath = copy(source_full_name, ITF)

                #print(source_full_name, f, match)
            # if f.endswith('.jpg'):
            #     i = Image.open(os.path.join(Source,f))
            #     fn, fext = os.path.splitext(f)

            #     if os.path.isfile(os.path.join(ITF_1024 + '/' + fn + '.png')):
            #         # file already exists there.
            #         pass
            #     else:
            #         i.save(ITF_1024 + '/{}.png'.format(fn))


if(__name__ == "__main__"):
    main()


