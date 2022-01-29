import cv2
import os
import time
import config
import contact
from twilio.rest import Client
from face_vision import FaceVision
from body_vision import BodyVision
from dotenv import load_dotenv



load_dotenv()

# -------VARIABLES-------#
# Process Window
faceview = FaceVision()
windowName = "Live Feed"
capture = cv2.VideoCapture(0)  # 0: Use default webcam
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
# cv2.createButton("Kill", Kill, None, cv2.QT_PUSH_BUTTON, 1)
cv2.resizeWindow(windowName, 640, 480)
client = Client(os.getenv('API_SID_TWILIO'), os.getenv('API_KEY_TWILIO'))

# Video Archiving
outFilename = 'data\\video_capture\\output_3.mp4'
codec = cv2.VideoWriter_fourcc(*'mp4v')
framerate = 15
resolution = (640, 480)
Output = cv2.VideoWriter(outFilename, codec, framerate / 1, resolution)


class VisionClient():

    #
    def __init__(self, connection_to='tcp://127.0.0.1:5555'):
        pass


    #
    def kill(*args):
        pass


    #
    def init_request_reply(self, connection):
        pass


    #
    def tracking(self):
        pass


    if capture.isOpened():
        returnVal, frame = capture.read()
    else:
        returnVal = False

    # -------Continue to retrieve, decode, and output subsequent video frames-------#

    while returnVal:
        ticks = cv2.getTickCount()
        returnVal, frame = capture.read()
        # contact.write()

        # -------FPS TICKER-------#
        fps = (cv2.getTickFrequency() / (cv2.getTickCount() - ticks))
        cv2.putText(frame, str(int(fps)), (5, 470), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        grayScale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Gray scale is a requirement for recognition
        bodies = config.fullBody_HarrCascade.detectMultiScale(grayScale, scaleFactor=1.3, minNeighbors=5)
        faces = config.face_HarrCascade.detectMultiScale(grayScale, scaleFactor=1.5, minNeighbors=5)
        faceProfiles = config.faceProfile_HarrCascade.detectMultiScale(grayScale, scaleFactor=1.3, minNeighbors=5)

        # -------Facial recognition and tracking-------#
        ImgFileName1 = faceview.faceShot(faces, frame)
        if (ImgFileName1): contact.reportcapture(ImgFileName1)

        ImgFileName2 = faceview.faceShot(faceProfiles, frame)
        if (ImgFileName2): contact.reportcapture(ImgFileName2)

        # -------Body recognition and tracking-------#
        # bodyview.bodyShot(bodies, frame)

        # -------Write to output video\update frome------- #
        cv2.putText(frame, "LIVE", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (50, 20, 255), 1)
        Output.write(frame)
        cv2.imshow(windowName, frame)

        # waitKey(1): for use in loops
        # waitKey() returns 32 bit value, key input (ASCII) is 8 bit -
        #   0xFF ignores all other values but last 8 to compare with ord('q').
        if cv2.waitKey(1) & 0xFF == ord('q'):
            client.messages.create(body=f"Camera Killed... \n Time: {time.asctime(time.localtime(time.time()))}", from_=os.getenv('SENDER_NUMBER'), to=os.getenv('RECEIVER_NUMBER'))
            break
        if cv2.waitKey(1) & 0xFF == ord('1'):
            print("hit 1")
            cv2.waitKey(0)
        # frame = frame_resize(frame, 1)
        if cv2.waitKey(1) & 0xFF == ord('2'):
            print("hit 2")
            cv2.waitKey(0)
        # frame = frame_resize(frame, 2)
        if cv2.waitKey(1) & 0xFF == ord('3'):
            print("hit 3")
            cv2.waitKey(0)
    # frame = frame_resize(frame, 3)

    # -------Clean Up-------#
    cv2.destroyAllWindows()
    Output.release()
    capture.release()
    exit()
