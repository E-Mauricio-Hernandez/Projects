import cv2
import numpy as np
from time import time

camara = cv2.VideoCapture ('VIDEOS/video32.mov')
cv2.namedWindow ('Video')

#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

kernel = np.ones((3,3),np.uint8)

while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 1)
	hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)

	mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
	mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	mask = cv2.add(mascara_rojo1, mascara_rojo2)
	mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
	mask = cv2.Canny(mask, 100, 200, 3)

    #Si el area blanca de la mascara es superior a 500px, no se trata de ruido
	imagen_contornos, contornos, jerarquia = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)	
	contorno = contornos[0]
	M = cv2.moments(contorno)
	area = cv2.contourArea(contorno)
	#areas = [cv2.contourArea(c) for c in contours]
    i = 0
    for extension in areas:
        if extension > 600:
            actual = contours[i]
            approx = cv2.approxPolyDP(actual,0.05*cv2.arcLength(actual,True),True)
            if len(approx)==3:
                cv2.drawContours(frame_bgr,[actual],0,(0,0,255),2)
                cv2.drawContours(mask,[actual],0,(0,0,255),2)
            i = i+1     
    cv2.imshow('mask', mask)
    cv2.imshow('Camara', frame_bgr)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break
   
cv2.destroyAllWindows()