import sys
from PIL import Image, ImageDraw
from google.cloud import vision


def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    content = face_file.read()
    image = vision.Client().image(content=content)

    return image.detect_faces()



def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.

    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the
          faces have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(bound.x_coordinate, bound.y_coordinate)
               for bound in face.bounds.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')
        print box

    im.save(output_filename)


def main(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)


def crop_square(input_filename, output_filename, crop_filename, max_results):
    main(input_filename,output_filename, crop_filename, max_results)
    img = Image.open(output_filename)
    ## need to update with extracting coordinates from the hightlight faces section
    img2 = img.crop((192,110,601,587))
    img2.save(crop_filename)








