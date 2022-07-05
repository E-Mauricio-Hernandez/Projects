import cv2
import numpy as np

def nothing (x):
	pass

#camara web
camara = cv2.VideoCapture (0)

#archivo .mov
#camara =cv2.VideoCapture ('videos/video1.mov')

cv2.namedWindow ('Video')

cv2.createTrackbar ('H min', 'Video', 40, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 50, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 50, 255, nothing)

cv2.createTrackbar ('H max', 'Video', 70, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)


while True:
	ret, frame_bgr = camara.read ()
	frame_hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)

	#mascara de color verde
	mascara = cv2.inRange (frame_hsv, 
		np.array ([cv2.getTrackbarPos ('H min', 'Video'), cv2.getTrackbarPos ('S min', 'Video'), cv2.getTrackbarPos ('V min', 'Video')]),
		np.array ([cv2.getTrackbarPos ('H max', 'Video'), cv2.getTrackbarPos ('S max', 'Video'), cv2.getTrackbarPos ('V max', 'Video')]))

	momentos = cv2.moments (mascara)
	print (momentos)

	x = int(momentos['m10'] / momentos['m00'])
	y = int(momentos['m01'] / momentos['m00'])
	print(x, ',', y)

	cv2.circle(frame_bgr, (x, y), 50, (0, 255, 0), 3)


	cv2.imshow ('Video', frame_bgr)
	cv2.imshow ('HSV', frame_hsv)
	cv2.imshow ('Imagen Mascara', mascara)

	if cv2.waitKey (1) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()

'''
#capturar imagen
imagen_rgb = input ('ruta de la imagen: ')
imagen_bgr = cv2.imread(imagen_rgb)

#convertir imagen de BGR a HSV
imagen_hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)

#verde inicial
verde_inicial = np.array ([40, 50, 50])

#verde final
verde_final = np.array ([70, 255, 255])

#mascara de color verde
mascara = cv2.inRange (imagen_hsv, verde_inicial, verde_final)

print(imagen_bgr[100, 100])
print(imagen_hsv[100, 100])


cv2.imshow ('Imagen BGR', imagen_bgr)
cv2.imshow ('Imagen HSV', imagen_hsv)
cv2.imshow ('Imagen Mascara', mascara)


cv2.waitKey ()
cv2.destroyAllWindows ()
'''