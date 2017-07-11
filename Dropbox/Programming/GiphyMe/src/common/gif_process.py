from PIL import Image, ImageDraw
import imageio


def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass


## script to breakapart gif images
im = Image.open('source.gif')
for i, frame in enumerate(iter_frames(im)):
    frame.save('test%d.jpg' % i,**frame.info)
    x = i



## script back into gif
filenames = []
i = 0
while i <= x:
    filenames.append('test%d.jpg' % i)
    i += 1


## Convert to JPEG... currently Vision doesn't seem to support PNG
images = []
for filename in filenames:
    im = Image.open(filename)


## Recompresses series of images back into a gif
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('output.gif', images)




# images = ['test0.jpg','test1.png','test2.png']
#
#
#
# print property(images[1])
# print images[1]
#
# Image.open(images[1])

# Image.open(images[1])


# images = []
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('output.gif', images)


