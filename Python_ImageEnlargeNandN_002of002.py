import os

from PIL import Image, ImageFilter
from DefaultItems import ImagesTestFolder as ITF

ITF_png = ITF + "\\" + "png"
print(ITF_png)

ITF_300 = ITF + "\\" + "300"
print(ITF_300)

ITF_768 = ITF + "\\" + "768"
print(ITF_768)

ITF_1200 = ITF + "\\" + "1200"
print(ITF_1200)

ITF_1024 = ITF + "\\" + "1024"
print(ITF_1024)


size_300 = (300,300)
size_1200 = (1200,1200)

def main():

    #
    # cycle over all files in folder 'ITF'
    #
    for f in os.listdir(ITF):
        #print("Line 28:", f, ITF)
        if f.lower().endswith('.jpg'):
            i = Image.open(os.path.join(ITF,f))
            fn, fext = os.path.splitext(f)

            if os.path.isfile(os.path.join(ITF_png + '/' + fn + '.png')):
                # file already exists there.
                pass
            else:
                i.save(ITF_png + '/{}.png'.format(fn))

            i.thumbnail(size_300)
            if os.path.isfile(os.path.join(ITF_300 + '/' + fn + '.png')):
                # file already exists there.
                pass
            else:
                i.save(ITF_300 + '/{}.png'.format(fn))

            i.thumbnail(size_1200)
            if os.path.isfile(os.path.join(ITF_1200 + '/' + fn + '.png')):
                # file already exists there.
                pass
            else:
                i.save(ITF_1200 + '/{}.png'.format(fn))

            basewidth = 1024
            #print("reached: 54")

            #print("56 - testing: ", os.path.join(ITF_1024 + '\\' + fn + '.png'))
            if os.path.isfile(os.path.join(ITF_1024 + '\\' + fn + '.png')):
                pass
                #print("reached: 57 exists", fn)
            else:
                wpercent = (basewidth/float(i.size[0]))
                hsize = int((float(i.size[1])*float(wpercent)))
                j = i.resize((basewidth, hsize), Image.ANTIALIAS)
                j.save(ITF_1024 + '/{}.png'.format(fn))
                print("saved:", j)
                #j.show()

            basewidth = 768
            #print("reached: 54")

            #print("56 - testing: ", os.path.join(ITF_1024 + '\\' + fn + '.png'))
            if os.path.isfile(os.path.join(ITF_768 + '\\' + fn + '.png')):
                pass
                #print("reached: 57 exists", fn)
            else:
                wpercent = (basewidth/float(i.size[0]))
                hsize = int((float(i.size[1])*float(wpercent)))
                j = i.resize((basewidth, hsize), Image.ANTIALIAS)
                j.save(ITF_768 + '/{}.png'.format(fn))
                print("saved:", j)
                #j.show()

if(__name__ == "__main__"):
    main()


