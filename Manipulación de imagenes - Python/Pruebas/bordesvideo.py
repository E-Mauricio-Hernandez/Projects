import cv2
import numpy as np
from time import time

def nothing (x):
	pass

camara = cv2.VideoCapture ('VIDEOS/video6.mov') ##29  ##32   ##6 30 11 amarillos ##verde 17 35
cv2.namedWindow ('Video')
'''
cv2.createTrackbar ('H min', 'Video', 49, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 50, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 50, 255, nothing)
cv2.createTrackbar ('H max', 'Video', 80, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)
'''
#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

#Nuevos verdes
verdes_bajos = np.array ([79, 82, 82])
verdes_altos = np.array ([90, 220, 220])

#Amarillos:
amarillo_bajos = np.array ([20, 100, 100])
amarillo_altos = np.array ([30, 255, 255])

kernel = np.ones((3,3),np.uint8)
while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 1)
	frame_bgr = frame_bgr[200:400, 0:]

	hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)
	'''
	Hmin = cv2.getTrackbarPos ('H min', 'Video')
	Smin = cv2.getTrackbarPos ('S min', 'Video')
	Vmin = cv2.getTrackbarPos ('V min', 'Video')
	Hmax = cv2.getTrackbarPos ('H max', 'Video')
	Smax = cv2.getTrackbarPos ('S max', 'Video')
	Vmax = cv2.getTrackbarPos ('V max', 'Video')
	'''
	#mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
	#mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	#mask = cv2.add(mascara_rojo1, mascara_rojo2)
	#mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)

	mask = cv2.inRange(hsv, verdes_bajos, verdes_altos)
	mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	#mask = cv2.erode (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (3, 3)), iterations = 1)
	#mask = cv2.Canny(mask, 100, 200, 3)
	#Detectamos contornos, nos quedamos con el mayor y calculamos su centro

	_, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#mayor_contorno=max(contours, key = cv2.contourArea)
	if len(contours) == 0:
		mayor_contorno = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno=max(contours, key = cv2.contourArea)
	#if mayor_contorno : (void)
		#print("vacio")
	print(mayor_contorno)
	#if mayor_contorno == null:

	momentos = cv2.moments(mayor_contorno)
	cx = int(momentos['m10']/momentos['m00'])
	cy = int(momentos['m01']/momentos['m00'])

	#cv2.circle (frame_bgr, (cx, cy), 30, (0, 255, 0), 2)

	# el momento 00 retorna el área
	area = momentos ['m00']
	# imprimimos el área
	#print ('area:', area)	
	if area > 1200: ##verdes 6200  ##amarillo 1200  ##5500
		if area < 3000:  ##verdes 12000 ##amarillo 3000  ##12000
			cx = int(momentos['m10']/momentos['m00'])
			cy = int(momentos['m01']/momentos['m00'])

			cv2.circle (frame_bgr, (cx, cy), 30, (0, 255, 0), 2)
			print(area)
	cv2.imshow ('frame_bgr', frame_bgr)
	#cv2.imshow ('frame_hsv', hsv)
	cv2.imshow ('mascara', mask)
	#cv2.imshow ('res', resultado)

	#cv2.imshow ('frame_roi', frame_roi)


	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()
