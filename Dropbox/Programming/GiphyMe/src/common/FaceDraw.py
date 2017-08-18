import io
import os
import src.Credentials


from google.cloud import vision

class FaceDraw(object):

    def __init__(self):
        pass

    def face_coordinates(self, file):
        vision_client = vision.Client('GiphyMe')

        file_name = os.path.join(
            os.path.dirname(__file__),
            file)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision_client.image(content=content)

        faces = image.detect_faces()
        print('Faces:')

        for face in faces:
            print('anger: {}'.format(face.emotions.anger))
            print('joy: {}'.format(face.emotions.joy))
            print('surprise: {}'.format(face.emotions.surprise))
            print('chin center: {}').format(face.landmarks.chin_gnathion.position.x_coordinate)
            print('chin left: {}').format(face.landmarks.chin_left_gonion.position.x_coordinate)
            print('chin right: {}').format(face.landmarks.chin_right_gonion.position.x_coordinate)
            print('nose tip: {}').format(face.landmarks.nose_tip.position.y_coordinate)

            vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
                         for bound in face.bounds.vertices])

            print vertices
            print type(vertices[0][:])

            print('face bounds: {}'.format(','.join(vertices)))

    def face_mark(self, file):
        vision_client = vision.Client('GiphyMe')

        file_name = os.path.join(
            os.path.dirname(__file__),
            file)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision_client.image(content=content)

        faces = image.detect_faces()
        face = faces[0]

        face_marks = {
            'chin_center_x': face.landmarks.chin_gnathion.position.x_coordinate,
            'chin_center_y': face.landmarks.chin_gnathion.position.y_coordinate,
            'chin_left_x': face.landmarks.chin_left_gonion.position.x_coordinate,
            'chin_left_y': face.landmarks.chin_left_gonion.position.y_coordinate,
            'chin_right_x': face.landmarks.chin_right_gonion.position.x_coordinate,
            'chin_right_y': face.landmarks.chin_right_gonion.position.y_coordinate,
            'right_ear_x': face.landmarks.right_ear_traigon.position.x_coordinate,
            'right_ear_y': face.landmarks.right_ear_traigon.position.y_coordinate,
            'left_ear_x': face.landmarks.left_ear_traigon.position.x_coordinate,
            'left_ear_y': face.landmarks.left_ear_traigon.position.y_coordinate
        }

        face_marks_2 = {
            'chin_center':[face.landmarks.chin_gnathion.position.x_coordinate,
                              face.landmarks.chin_gnathion.position.y_coordinate],
            'chin_left':[face.landmarks.chin_left_gonion.position.x_coordinate,
                          face.landmarks.chin_left_gonion.position.y_coordinate]
        }
        print face_marks_2['chin_center'][0]
        print face_marks
        return face_marks


    # def draw_mark(self):

        #
        # print('Faces:')t
        #
        # for face in faces:
        #     print('anger: {}'.format(face.emotions.anger))
        #     print('joy: {}'.format(face.emotions.joy))
        #     print('surprise: {}'.format(face.emotions.surprise))
        #     print('chin center: {}').format(face.landmarks.chin_gnathion.position.x_coordinate)
        #     print('chin left: {}').format(face.landmarks.chin_left_gonion.position.x_coordinate)
        #     print('chin right: {}').format(face.landmarks.chin_right_gonion.position.x_coordinate)
        #     print('nose tip: {}').format(face.landmarks.nose_tip.position.y_coordinate)
        #
        #     vertices = (['({},{})'.format(bound.x_coordinate, bound.y_coordinate)
        #                  for bound in face.bounds.vertices])
        #
        #     print('face bounds: {}'.format(','.join(vertices)))






                    #
        #
        # with io.open(file_name, 'rb') as image_file:
        #     content = image_file.read()
        #     image = vision_client.image(
        #         content=content)

        # faces = image.detect_faces(limit=10)
        # bounds = image.detect_properties()
        #
        #
        #
        # first_face = faces[0]
        # print first_face.bound.x_coordinate
        #
        #
        # print first_face.landmarks.left_eye.position.x_coordinate
        # print first_face.detection_confidence
        # print first_face.joy
        # print first_face.anger
        # print first_face.landmarks.left_eye.position.x_coordinate
        # print first_face.landmarks.right_eye.position.x_coordinate

