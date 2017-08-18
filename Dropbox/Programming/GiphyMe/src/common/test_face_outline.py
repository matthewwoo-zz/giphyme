from PIL import Image

import src.common.face_methods as fc
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



selfie_image = fc.outline_face('test.jpg',1)
selfie_crop = fc.crop_face(image=selfie_image.image,
                           face_coordinates=selfie_image.face_coordinates,
                           output_filename="test_crop.jpg")
