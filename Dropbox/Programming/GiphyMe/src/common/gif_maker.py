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


## Expand gif into frames
def expand_gif(input_filename):
    im = Image.open(input_filename)
    gif_images = []
    for i, frame in enumerate(iter_frames(im)):
        frame.save('gif%d.png' % i,**frame.info)
        gif_images.append('gif%d.png' % i)
    return gif_images


## Create images from
def create_gif(gif_images, output_filename):
    images = []
    for filename in gif_images:
        images.append(imageio.imread(filename))
    imageio.mimsave(output_filename, images)

gif_images = expand_gif('source.gif')
create_gif(gif_images, 'new.gif')



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


