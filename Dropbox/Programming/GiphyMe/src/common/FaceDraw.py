import io
import os
import src.Credentials


from google.cloud import vision

class FaceDraw(object):

    def __init__(self):
        pass

    def coordinates(self, file):
        vision_client = vision.Client('GiphyMe')

        file_name = os.path.join(
            os.path.dirname(__file__),
            file)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
            image = vision_client.image(
                content=content)

        faces = image.detect_faces(limit=10)

        first_face = faces[0]
        print first_face.fd_bounds.__dict__
        print ('Dump')
        print ('All Attributes')
        print vars(first_face)
        print ('Bounds')
        print vars(first_face.bounds)
        print ('Face Bounds')
        print vars(first_face.fd_bounds)
        print first_face.__str__

        print first_face.landmarks.left_eye.position.x_coordinate
        print first_face.detection_confidence
        print first_face.joy
        print first_face.anger
        print first_face.landmarks.left_eye.position.x_coordinate
        print first_face.landmarks.right_eye.position.x_coordinate


    def detect_crop_hints(self, file):
        vision_client = vision.Client()

        file_name = os.path.join(
            os.path.dirname(__file__),
            file)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision_client.image(content=content)

        hints = image.detect_crop_hints({1.77})

        for n, hint in enumerate(hints):
            print('\nCrop Hint: {}'.format(n))

            vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                         for bound in hint.bounds.vertices])

            print('bounds: {}'.format(','.join(vertices)))