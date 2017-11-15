from PIL import Image

import src.common.face_methods as fc
import src.common.gif_maker as gm
import os

'''
Single Paste
- Identify face on selfie and crop
- Split GIF into multiple frames
- Identify face on GIF and get coordinates on first Frame
- Normalize two images and resized cropped selfie
  - Sample coordinates [192 (x1), 110(y1), 601(x2), 587(y2)]
  - To calculate height
        - (110-587)
  - To calculate width
        - (192-601)
- Paste resized cropped seflie on GIF Image
'''

# def giphy_me(selfie_img, gif):
#     selfie_image_cd = fc.outline_face(selfie_img, 1)
#     fc.crop_face(input_filename=selfie_img, face_coordinates=selfie_image_cd, output_filename="selfie_crop.jpg")
#     gif_images = gm.expand_gif(gif)
#     new_gif_images =[]
#     i = 0
#     for filename in gif_images:
#         try:
#             print filename
#             gif_face_coordinates = fc.outline_face(filename, 1)
#             fc.resize_image('selfie_crop.jpg', 'selfie_resize.png', gif_face_coordinates)
#             selfie = Image.open('selfie_resize.png').convert('RGBA')
#             gif_image = Image.open(filename).convert('RGBA')
#             gif_face_coordinates = fc.outline_face(filename, 1)
#             gif_image.paste(selfie, (gif_face_coordinates[0], gif_face_coordinates[1],gif_face_coordinates[2],gif_face_coordinates[3]))
#             gif_image.save('giphy_me_%d.png' % i)
#             new_gif_images.append('giphy_me_%d.png' % i)
#             i += 1
#         except:
#             pass
#     gm.create_gif(new_gif_images,'giphy_me_1.gif')
#
#
# giphy_me('anthony.jpg','chris.gif')

def giphy_me_test(selfie_img, gif):
    selfie_image_cd = fc.outline_face(selfie_img, 1)
    fc.crop_face(input_filename=selfie_img, face_coordinates=selfie_image_cd, output_filename="selfie_crop.jpg")
    gif_images, test_folder = gm.expand_gif(gif)
    new_gif_images = []
    i = 0
    for filename in gif_images:
        try:
            print filename
            gif_face_coordinates = fc.outline_face(test_folder+'/'+filename, 1)
            fc.resize_image('selfie_crop.jpg', 'selfie_resize.png', gif_face_coordinates)
            selfie = Image.open('selfie_resize.png').convert('RGBA')
            gif_image = Image.open(test_folder+'/'+filename).convert('RGBA')
            gif_face_coordinates = fc.outline_face(test_folder+'/'+filename, 1)
            gif_image.paste(selfie, (gif_face_coordinates[0], gif_face_coordinates[1],gif_face_coordinates[2],gif_face_coordinates[3]))
            gif_image.save(test_folder+'/giphy_me_%d.png' % i)
            new_gif_images.append(test_folder+'/giphy_me_%d.png' % i)
            i += 1
        except:
            pass
    gm.create_gif(new_gif_images,'giphy_me_1.gif')
    files = ['selfie_crop.jpg','selfie_resize.png']
    clean(files)
    return 200

def clean(files):
    path = os.getcwd()
    for i in files:
        os.remove(path+"/"+i)
    return 200

giphy_me_test('Profile_Photo.png','giphy.gif')