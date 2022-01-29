import os
import cv2


#-------GLOBAL VARIABLES-------#
APP_FOLDER              = os.getcwd()
APP_FOLDER_FACES        = APP_FOLDER + f"\\data\\images\\Faces_Captured\\"
APP_FOLDER_BODIES       = APP_FOLDER + f"\\data\\images\\Bodies_Captured\\"
total_files_faces       = 0
total_files_bodies      = 0


fullBody_HarrCascade    = cv2.CascadeClassifier('data\\Haar\\data\\haarcascade_fullbody.xml')           # Body recognition algorithms
face_HarrCascade        = cv2.CascadeClassifier('data\\Haar\\data\\haarcascade_frontalface_alt.xml')    # Facial recognition algorithms
faceProfile_HarrCascade = cv2.CascadeClassifier('data\\Haar\\data\\haarcascade_profileface.xml')        # Total Facial Profile recognition algorithms
