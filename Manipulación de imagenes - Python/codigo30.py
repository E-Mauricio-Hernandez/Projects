import cv2
import numpy as np

#archivo .mov
camara =cv2.VideoCapture ('VIDEOS/video4.mov')

verde_inicial = np.array ([40, 50, 50])
verde_final = np.array ([80, 255, 255])

while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	
	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 0)
	frame_hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)
	# Mascara que guarde los pixeles de color definido, segun intervalo definido
	mascara_verde = cv2.inRange (frame_hsv, verde_inicial, verde_final)

	frame_roi = frame_bgr[0:500, 0:400, 0]

	cv2.imshow ('frame_bgr', frame_bgr)
	cv2.imshow ('frame_hsv', frame_hsv)
	cv2.imshow ('mascara_verde', mascara_verde)
	cv2.imshow ('frame_roi', frame_roi)


	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()