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

# def outline_face(faces):
#     """Marks coordinate of face.
#     """
#     for face in faces:
#         box = [(bound.x_coordinate, bound.y_coordinate)
#                for bound in face.bounds.vertices]
#     face_coordinates = [box[0][0],box[0][1], box[2][0], box[2][1]]
#     print face_coordinates
#     return face_coordinates

def outline_face(input_filename, max_results):
    with open(input_filename) as image:
        faces = detect_face(image, max_results)
        if faces.__len__() == 0:
            return False
        else:
            print('Found {} face{}'.format(
                len(faces), '' if len(faces) == 1 else 's'))
            # Reset the file pointer, so we can read the file again
            image.seek(0)
            for face in faces:
                box = [(bound.x_coordinate, bound.y_coordinate)
                       for bound in face.bounds.vertices]
            face_coordinates = [box[0][0], box[0][1], box[2][0], box[2][1]]
            return face_coordinates

def crop_face(input_filename,face_coordinates, output_filename):
    img = Image.open(input_filename)
    img2 = img.crop(face_coordinates)
    img2.save(output_filename)
    return True

def outline_face_image(faces):
    for face in faces:
        box = [(bound.x_coordinate, bound.y_coordinate)
               for bound in face.bounds.vertices]
    face_coordinates = [box[0][0], box[0][1], box[2][0], box[2][1]]
    return face_coordinates

def resize_image(input_filename,output_filename, face_coordinates):
    height = face_coordinates[3] - face_coordinates[1]
    width = face_coordinates[2] - face_coordinates[0]
    img = Image.open(input_filename)
    resize_img = img.resize((width, height), resample=0)
    resize_img.save(output_filename)

# face_coordinates = [10,10,100,70]
# resize_image('test_crop.jpg','test_resize.jpg',face_coordinates)



