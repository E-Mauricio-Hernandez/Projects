import cv2
import numpy as np
from time import time


#archivo .mov
imagen_bgr = cv2.imread('señalverde.png')
#imagen_bgr = imagen_bgr[0:700, 0:700]
imagen_bgr = imagen_bgr[200:500, 0:]

imagen_gris = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.uint8)
imagen_contorno = np.ones((imagen_gris.shape[0], imagen_gris.shape[1]), dtype=np.uint8)
imagen_rectangulo_envolvente = np.ones((imagen_gris.shape[0], imagen_gris.shape[1]), dtype=np.uint8)

#camara = cv2.VideoCapture ('VIDEOS/video2.mov')

hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)

#cv2.namedWindow ('Video')
#camara = cv2.VideoCapture (0)
#bordes = cv2.Canny(imagen_gris, 100, 200, 3)

#Nuevos verdes
verdes_bajos = np.array ([49, 82, 82])
verdes_altos = np.array ([120, 220, 220])

#Azules:
azul_bajos = np.array([100,65,75], dtype=np.uint8)
azul_altos = np.array([130, 255, 255], dtype=np.uint8)
#mascara_verde = cv2.inRange(hsv, verde_bajos, verde_altos)

#Amarillos:
amarillo_bajos = np.array ([20, 100, 100])
amarillo_altos = np.array ([30, 255, 255])


#Detectar los pixeles de la imagen que esten dentro del rango de amarillos
#mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
#mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
#mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
#mask = cv2.add(mascara_rojo1, mascara_rojo2)
#mask = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
mask = cv2.inRange(hsv, verdes_bajos, verdes_altos)
#mask = cv2.inRange(hsv, azul_bajos, azul_altos)

mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.Canny(mask, 100, 200, 3)	

figura = cvApproxPoly(mask)
print(figura)
#Detectar y guardar los contornos. Tambien sus areas.
_,contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
areas = [cv2.contourArea(c) for c in contours]

i = 0
for extension in areas:
	if extension > 300:
		actual = contours[i]
		approx = cv2.approxPolyDP(actual,0.05*cv2.arcLength(actual,True),True)
		print(approx)
		if len(approx)==4:
			cv2.drawContours(imagen_bgr,[actual],0,(0,0,255),2)
			cv2.drawContours(mask,[actual],0,(0,0,255),2)
		i = i+1
#mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)

momentos = cv2.moments (mask)

	# el momento 00 retorna el área
area = momentos ['m00']
	# imprimimos el área
print ('area:', area)	
if area > 1830:
	#if area < 801830:
	cx = int(momentos['m10']/momentos['m00'])
	cy = int(momentos['m01']/momentos['m00'])

	cv2.circle (imagen_bgr, (cx, cy), 30, (0, 255, 0), 2)

cv2.imshow ('frame_bgr', imagen_bgr)
cv2.imshow ('mascara', mask)


while(1):
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows ()

