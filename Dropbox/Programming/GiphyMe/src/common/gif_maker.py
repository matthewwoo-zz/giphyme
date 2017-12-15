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


## Expand gifs into frames with temp folder
def expand_gif(input_filename):
    im = Image.open(input_filename)
    test_folder = tp.mkdtemp()
    gif_images = []
    for i, frame in enumerate(iter_frames(im)):
        frame.save(test_folder + '/gifs%d.png' % i, **frame.info)
        gif_images.append('gifs%d.png' % i)
    print os.listdir(test_folder)
    print test_folder
    return gif_images, test_folder


## Create images from
def create_gif(gif_images, output_filename):
    images = []
    for filename in gif_images:
        images.append(imageio.imread(filename))
    imageio.mimsave(output_filename, images)


## Expand gifs into frames old method with no temp folders
# def expand_gif_old(input_filename):
#     im = Image.open(input_filename)
#     gif_images = []
#     for i, frame in enumerate(iter_frames(im)):
#         frame.save('gifs%d.png' % i, **frame.info)
#         gif_images.append('gifs%d.png' % i)
#     return gif_images

# test = expand_gif('new.gifs')
# create_gif(test,'new_1.gifs')