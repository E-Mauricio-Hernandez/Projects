import cv2
import numpy as np
from time import time
##funcion para la barra
def nothing (x):
	pass

#archivo .mov
camara = cv2.VideoCapture ('VIDEOS/video2.mov')
#verde_bajos = np.array([86,140,140])
#verde_altos = np.array([95, 255, 255])
cv2.namedWindow ('Video')
#camara = cv2.VideoCapture (0)
#bordes = cv2.Canny(imagen_gris, 100, 200, 3)

#Verdes
#verde_inicial = np.array ([40, 50, 50])
#verde_final = np.array ([80, 255, 255])

#Rojos:
rojo_bajos1 = np.array([0,65,75], dtype=np.uint8)
rojo_altos1 = np.array([12, 255, 255], dtype=np.uint8)
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

kernel = np.ones((3,3),np.uint8)

#Creamos los controles para definir el color a seguir
'''
cv2.createTrackbar ('H min', 'Video', 86, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 140, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 140, 255, nothing)
cv2.createTrackbar ('H max', 'Video', 95, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)

'''

while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 0)
	frame_hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)
	#capturamos el valor de cada variable del HSV para los intervalos
	'''
	Hmin = cv2.getTrackbarPos ('H min', 'Video')
	Smin = cv2.getTrackbarPos ('S min', 'Video')
	Vmin = cv2.getTrackbarPos ('V min', 'Video')
	Hmax = cv2.getTrackbarPos ('H max', 'Video')
	Smax = cv2.getTrackbarPos ('S max', 'Video')
	Vmax = cv2.getTrackbarPos ('V max', 'Video')
	'''
	# Mascara que guarde los pixeles de color definido, segun intervalo definido
	#mascara_verde = cv2.inRange (frame_hsv, verde_inicial, verde_final)
	#mascara del color
	#mascara = cv2.inRange (frame_hsv, np.array ([Hmin, Smin, Vmin]), np.array ([Hmax, Smax, Vmax]))
	mascara_rojo1 = cv2.inRange(frame_hsv, rojo_bajos1, rojo_altos1)
	mascara_rojo2 = cv2.inRange(frame_hsv, rojo_bajos2, rojo_altos2)
	mascara = cv2.add(mascara_rojo1, mascara_rojo2)
	bordes = cv2.Canny(mascara, 100, 200, 3)

	#frame_roi = frame_bgr[0:500, 0:400, 0]
	#eliminar ruido de la mascara
	#mascara = cv2.erode (mascara, cv2.getStructuringElement (cv2.MORPH_RECT, (3, 3)), iterations = 1)
	mascara = cv2.dilate (mascara, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
	mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
	#calculamos los momentos
	momentos = cv2.moments (mascara)

	#si el area del objeto es superior a 50000 pixeles se deja
	if momentos ['m00'] > 2000000:
		#calculamos el centroide del objeto
		x = int (momentos ['m10'] / momentos ['m00'])
		y = int (momentos ['m01'] / momentos ['m00'])
		area = momentos['m00']
		print(area)
		#mostrar un circulo verde
		cv2.circle (frame_bgr, (x, y), 30, (0, 255, 0), 2)
	cv2.imshow ('frame_bgr', frame_bgr)
	cv2.imshow ('frame_hsv', frame_hsv)
	cv2.imshow ('mascara', mascara)
	#cv2.imshow ('frame_roi', frame_roi)


	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()


##cebra
#gradiente = cv2.dilate(imagen_gris, kernel, iterations = 1) - cv2.erode(imagen_gris, kernel, iterations = 1)