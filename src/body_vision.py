import cv2
import os
import config
import helper



# -------VARIABLES-------#



class BodyVision():

	# -------Body recognition and tracking-------#
	def __init__(self):
		pass


	def bodyShot(self, bodies, frame):
		grayScale               = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Gray scale is a requirement for recognition
		photo_box_color_body    = (255, 50, 80)

		i = 1
		# overlap = []
		for (body_x, body_y, body_width, body_height) in bodies:
			start_coords_body       = (body_x, body_y)
			end_coords_body         = ((body_x + body_width), (body_y + body_height))
			start_dimensions_body   = (body_width, body_height)
			print(start_coords_body, start_dimensions_body)

			# -------Bodyshot container-------#
			bodyBox = cv2.rectangle(frame, start_coords_body, end_coords_body, photo_box_color_body, 2)
			cv2.putText(bodyBox, f'#{i}', (body_x, body_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 20, 50), 1)

			# -------Save faces recognized-------#
			interest_area_grey_body             = grayScale[body_y:body_y + body_height, body_x:body_x + body_width]
			interest_area_box_body              = frame[body_y:body_y + body_height, body_x:body_x + body_width]
			interest_area_fullContext_bodies    = frame
			sample_image_body                   = config.APP_FOLDER_BODIES + f"body_img-{config.total_files_bodies}.jpg"
			sample_image_grey_body              = config.APP_FOLDER_BODIES + f"body_grey_img-{config.total_files_bodies}.jpg"
			sample_image_fullContext_body       = config.APP_FOLDER_BODIES + f"body_context_img-{config.total_files_bodies}.jpg"

			if (os.path.isfile(sample_image_body)):
				print("body image number exists")
				while (True):
					config.total_files_bodies = config.total_files_bodies + 1
					if (not os.path.isfile(config.APP_FOLDER_BODIES + f"body_img-{config.total_files_bodies}.jpg")):
						print(sample_image_body)
						sample_image_body               = config.APP_FOLDER_BODIES + f"body_img-{config.total_files_bodies}.jpg"
						sample_image_grey_body          = config.APP_FOLDER_BODIES + f"body_grey_img-{config.total_files_bodies}.jpg"
						sample_image_fullContext_body   = config.APP_FOLDER_BODIES + f"body_context_img-{config.total_files_bodies}.jpg"
						config.total_files_bodies       = config.total_files_bodies + 1
						break

			cv2.imwrite(sample_image_body, interest_area_box_body, [int(cv2.IMWRITE_JPEG_QUALITY), 120])
			cv2.imwrite(sample_image_grey_body, interest_area_grey_body, [int(cv2.IMWRITE_JPEG_QUALITY), 120])
			cv2.imwrite(sample_image_fullContext_body, interest_area_fullContext_bodies, [int(cv2.IMWRITE_JPEG_QUALITY), 120])

			cv2.waitKey(5)
