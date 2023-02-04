import os
from PIL import Image, ImageFilter
from DefaultItems import ImagesFolder

def main():
    filename = "Hillary.jpg"

    filename_one = os.path.join(ImagesFolder,filename)

    print(filename_one)

    size = 160*3, 90*3
    image = Image.new( "RGB", size, "rgb(205,150,200)" )
    #image.show()
    #del image

    image = Image.open( filename_one, "r")
    size = width, height = image.size
    image.thumbnail((22128, 22128))
    #image.show()
    # mode - how colors are represented: 1 L, RGB RGBA, CMYK, YCbCr, I, F


    filename_two = ImagesFolder + "/Hillary.jpg"
    image_one = Image.open( filename_one )
    image_two = Image.open( filename_two)

    image_blended = Image.blend( image_one, image_two, 0.5 )
    #image_blended.show()

    #image_composite = Image.composite( image_one, image_two, image_two )
    #image_composite.show()

    '''
    image.filter( ImageFilter.BLUR).show()
    image.filter( ImageFilter.CONTOUR).show()
    image.filter( ImageFilter.DETAIL).show()
    image.filter( ImageFilter.EDGE_ENHANCE).show()
    image.filter( ImageFilter.EDGE_ENHANCE_MORE).show()
    image.filter( ImageFilter.EMBOSS).show()
    image.filter( ImageFilter.FIND_EDGES).show()
    image.filter( ImageFilter.SMOOTH).show()
    image.filter( ImageFilter.SMOOTH_MORE).show()
    image.filter( ImageFilter.SHARPEN).show()
'''
    suze = width, height = image.size
    print("Image_Size: ", image.size)

    coordinate = x, y = 180, 70
    print("getpixel: ", image.getpixel(coordinate)) # getdata is faster ...
    print("getcolors: ", image.getcolors(width * height))

    print("list_getdata: ", list(image.getdata()))
    image.paste( "green", (80, 20, 180, 200) )
    image.show()

    image.thumbnail((1128,1128 ), Image.NEAREST)
    image.show()

    image.resize((500,100)).show() # distorts

    color_to_find = (0,0,0,0)
    color_to_find = (0,0,0)
    color_to_replace = (255,255,255,255)
    color_to_replace = (255,255,255)

    rotated_image = image.rotate( 45 )
    #print(list(rotated_image.getdata()))

    new_image_data = []
    for color in list( rotated_image.getdata() ):
        if ( color == color_to_find):
            new_image_data += [ color_to_replace ]
        else:
            new_image_data += [ color ]

    rotated_image.putdata(new_image_data)

    rotated_image.show()

    filename_one = os.path.join(ImagesFolder,"Hillary_Tilted.png")

    rotated_image.save(filename_one)

    print(width)
    for x, y in range( width, height):
        image.putpixel( (x/2, y/2), ( 0,0, 0,255) ) # is slow

    print(list(rotated_image.getdata()))

    filename_one = os.path.join(ImagesFolder,"modified_ken.jpg")
    image.save(filename_one)


    del rotated_image
if(__name__ == "__main__"):
    main()


