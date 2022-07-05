import cv2
import numpy as np
from time import time

camara = cv2.VideoCapture ('VIDEOS/video29.mov')

#imagen_bgr = cv2.imread('figuras.png')
#imagen_hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)
while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;
	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 0)

	frame_bgr = frame_bgr[200:500, 0:]

	cv2.imshow ('frame_bgr', frame_bgr)

	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()