from PIL import Image

import src.common.face_detect_crop as fc
import src.common.gif_maker as gm

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


seflie_image = fc.detect_crop('test.jpg','test_crop.jpg',1)
# gm.expand_gif('source.gif')
gif_face_coordinates = fc.outline_face_image('gif0.png')
print gif_face_coordinates[0]
print gif_face_coordinates[1]
resize_selfie_image = fc.resize_image('test_crop.jpg','test_resize.png',gif_face_coordinates)
gif_image = Image.open('gif0.png').convert('RGBA')
selfie = Image.open('test_resize.png').convert('RGBA')
gif_image.paste(selfie, (gif_face_coordinates[0], gif_face_coordinates[1],gif_face_coordinates[2],gif_face_coordinates[3]))
gif_image.save('giphy_me_0.png')


