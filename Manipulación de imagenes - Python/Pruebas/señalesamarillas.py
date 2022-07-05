import cv2
import numpy as np
from time import time

def nothing (x):
	pass

camara = cv2.VideoCapture ('VIDEOS/video6.mov') ##29
cv2.namedWindow ('Video')
'''
cv2.createTrackbar ('H min', 'Video', 49, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 50, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 50, 255, nothing)
cv2.createTrackbar ('H max', 'Video', 80, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)
'''
#Amarillos:
amarillo_bajos = np.array ([20, 100, 100])
amarillo_altos = np.array ([30, 255, 255])

#Verdes
verde_bajos = np.array ([49, 50, 50])
verde_altos = np.array ([107, 255, 255])

#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)

#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)
rojo_bajos3 = np.array([153, 82, 0], dtype=np.uint8)
rojo_altos3 = np.array([180, 236, 49], dtype=np.uint8)
#blancos
blanco_bajos = np.array([54,0,216], dtype=np.uint8)
blanco_altos = np.array([77,15,239], dtype=np.uint8)
#blanco_bajos1 = np.array([92,22,143], dtype=np.uint8)
#blanco_altos1 = np.array([98,34,159], dtype=np.uint8)
#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)

#Naranjas
naranja_bajos = np.array([5,100,138], dtype=np.uint8)
naranja_altos = np.array([13, 255, 255], dtype=np.uint8)

kernel = np.ones((3,3),np.uint8)
while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 1)
	frame_bgr = frame_bgr[180:500, 0:]

	hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)
	'''
	Hmin = cv2.getTrackbarPos ('H min', 'Video')
	Smin = cv2.getTrackbarPos ('S min', 'Video')
	Vmin = cv2.getTrackbarPos ('V min', 'Video')
	Hmax = cv2.getTrackbarPos ('H max', 'Video')
	Smax = cv2.getTrackbarPos ('S max', 'Video')
	Vmax = cv2.getTrackbarPos ('V max', 'Video')
	'''
	mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
	#mask = cv2.inRange(hsv, azul_bajos, azul_altos)
	#mask = cv2.inRange(hsv, blanco_bajos, blanco_altos)
	#mask = cv2.inRange(hsv, blanco_bajos, blanco_altos)
	#mask = cv2.inRange(hsv, naranja_bajos, naranja_altos)

	#mascara_blanco2 = cv2.inRange(hsv, blanco_bajos1, blanco_altos1)
	#mask = cv2.add(mascara_blanco1, mascara_blanco2)

	#mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
	#mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	#mascara_rojo3 = cv2.inRange(hsv, rojo_bajos3, rojo_altos3)

	#mask = cv2.add(mascara_rojo1, mascara_rojo2,mascara_rojo3)
	#mask = cv2.inRange(hsv, verde_bajos, verde_altos)
	#mask = cv2.inRange (hsv, np.array ([Hmin, Smin, Vmin]), np.array ([Hmax, Smax, Vmax]))

	mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	#mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 2)

	#mask = cv2.erode (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (3, 3)), iterations = 1)
	#mask = cv2.Canny(mask, 100, 200, 3)
	_,contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	if len(contours) == 0:
		mayor_contorno = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno = max(contours, key = cv2.contourArea)

	'''
	areas = [cv2.contourArea(c) for c in contours]
	i = 0
	for extension in areas:
		if extension > 300:
			actual = contours[i]
			approx = cv2.approxPolyDP(actual,0.05*cv2.arcLength(actual,True),True)
			if len(approx)>2 and cv2.isContourConvex(approx) and cv2.contourArea(approx) > 70000:
				cv2.drawContours(frame_bgr,[actual],0,(0,0,255),2)
				cv2.drawContours(mask,[actual],0,(0,0,255),2)
			i = i+1
			'''
	#mayor_contorno = max(contours, key = cv2.contourArea)
	momentos = cv2.moments (mayor_contorno)
	#print(cv2.arcLength(mayor_contorno, True))

	# el momento 00 retorna el área
	area = momentos ['m00']
	# imprimimos el área
	#print ('area:', area)	
	if area > 2500 :
		if area < 7500:
			approx = cv2.approxPolyDP(mayor_contorno,0.05*cv2.arcLength(mayor_contorno,True),True)

			if len(approx) > 3:
				print(len(approx))
			#if (cv2.arcLength(mayor_contorno, True)) > 250:
				#print(approx)
				cx = int(momentos['m10']/momentos['m00'])
				cy = int(momentos['m01']/momentos['m00'])
				print("area",area)
				
				
				#print(cv2.arcLength(mayor_contorno, True))

				cv2.circle (frame_bgr, (cx, cy), 30, (0, 255, 0), 2)

	cv2.imshow ('frame_bgr', frame_bgr)
	#cv2.imshow ('frame_hsv', hsv)
	cv2.imshow ('mascara', mask)
	#cv2.imshow ('res', resultado)

	#cv2.imshow ('frame_roi', frame_roi)


	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()	