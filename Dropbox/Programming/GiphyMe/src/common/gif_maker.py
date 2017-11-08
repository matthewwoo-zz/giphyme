from PIL import Image, ImageDraw
import tempfile as tp
import imageio
import os


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

def test_gif(input_filename):
    im = Image.open(input_filename)
    test_folder = tp.mkdtemp()
    gif_images = []
    for i, frame in enumerate(iter_frames(im)):
        frame.save(test_folder +'/gif%d.png' % i, **frame.info)
        gif_images.append('gif%d.png' % i)
    print os.listdir(test_folder)
    return gif_images, test_folder



test_gif('giphy.gif')


# test = expand_gif('new.gif')
# create_gif(test,'new_1.gif')