import os
import sys
from PIL import Image, ImageDraw
from src.common.FaceDraw import FaceDraw

face = FaceDraw()
face.coordinates('test.jpg')
face.detect_crop_hints('test.jpg')







