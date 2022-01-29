import cv2
import numpy
import socket
import sys
import struct



HOSTNAME = ''
PORTNUMBER = 8090
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)