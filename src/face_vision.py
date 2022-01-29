import cv2
import os
import config
import helper



# -------VARIABLES-------#


class FaceVision():

    # -------Facial recognition and tracking-------#
    def __init__(self):
        pass


    def faceShot(self, faces, frame):
        grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Gray scale is a requirement for recognition
        photo_box_color_face = (80, 50, 255)

        i = 1
        # overlap = []
        for (facial_x, facial_y, facial_width, facial_height) in faces:
            start_coords_face = (facial_x, facial_y)
            end_coords_face = ((facial_x + facial_width), (facial_y + facial_height))
            start_dimensions_face = (facial_width, facial_height)
            print(start_coords_face, start_dimensions_face)

            # if not (start_coords_face, start_dimensions_face) in overlap:
            #     overlap.append((start_coords_face, start_dimensions_face))
            print(f"Unique: {start_coords_face, start_dimensions_face}")
            # -------Headshot container-------#
            photoBox = cv2.rectangle(frame, start_coords_face, end_coords_face, photo_box_color_face, 2)
            cv2.putText(photoBox, f'{i}', (facial_x, facial_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 20, 255), 2)

            # -------Save faces recognized-------#
            interest_area_grey_face = grayScale[facial_y:facial_y + facial_height, facial_x:facial_x + facial_width]
            interest_area_box_face = frame[facial_y:facial_y + facial_height, facial_x:facial_x + facial_width]
            interest_area_fullContext_face = frame
            sample_image_face = config.APP_FOLDER_FACES + f"facial_img-{config.total_files_faces}.jpg"
            sample_image_grey_face = config.APP_FOLDER_FACES + f"facial_grey_img-{config.total_files_faces}.jpg"
            sample_image_fullContext_face = config.APP_FOLDER_FACES + f"facial_context_img-{config.total_files_faces}.jpg"

            if (os.path.isfile(sample_image_face)):
                print("face image number exists")
                while (True):
                    config.total_files_faces = config.total_files_faces + 1
                    if (not os.path.isfile(config.APP_FOLDER_FACES + f"facial_img-{config.total_files_faces}.jpg")):
                        print(sample_image_face)
                        sample_image_face = config.APP_FOLDER_FACES + f"facial_img-{config.total_files_faces}.jpg"
                        sample_image_grey_face = config.APP_FOLDER_FACES + f"facial_grey_img-{config.total_files_faces}.jpg"
                        sample_image_fullContext_face = config.APP_FOLDER_FACES + f"facial_context_img-{config.total_files_faces}.jpg"
                        config.total_files_faces = config.total_files_faces + 1
                        break

            cv2.imwrite(sample_image_face, interest_area_box_face, [int(cv2.IMWRITE_JPEG_QUALITY), 120])
            cv2.imwrite(sample_image_grey_face, interest_area_grey_face, [int(cv2.IMWRITE_JPEG_QUALITY), 120])
            cv2.imwrite(sample_image_fullContext_face, interest_area_fullContext_face, [int(cv2.IMWRITE_JPEG_QUALITY), 120])

            image = cv2.imread(sample_image_fullContext_face, cv2.IMREAD_UNCHANGED)
            cv2.imwrite(sample_image_fullContext_face, image, [int(cv2.IMWRITE_JPEG_QUALITY), 120])

            return sample_image_fullContext_face
