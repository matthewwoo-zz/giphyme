import sys
from PIL import Image, ImageDraw


im = Image.open('/Users/mattw/Dropbox/Programming/GiphyMe/src/profile.jpg')

draw = ImageDraw.Draw(im)
draw.line((0,0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0],0), fill=128)
draw.ellipse(((10,10),(30,30)), fill=128)
im.save("test_point_1.jpg")


im.save(sys.stdout, "PNG")


