import io
import os
import json
from google.cloud import vision

def Selfie(object):

    def __init__(self, name, emotion, image):
        self.name = name
        self.emotion = emotion
        pass

    def json(self):
        return {
            'name': self.name,
            'emotion': self.emotion
        }


    def coordinates(file_name):
        vision_client = vision.Client('GiphyMe')

        file_name = os.path.join(
            os.path.dirname(__file__),
            'oprah.jpg')

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
        print first_face.landmarks.left_ear_tragion.position.x_coordinate








# print('Faces:')
# for face in faces:
#     print(faces.description)w