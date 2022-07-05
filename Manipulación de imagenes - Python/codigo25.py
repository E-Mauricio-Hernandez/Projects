import cv2
import numpy as np
import time


#capturar imagen
imagen_bgr = cv2.imread('figuras.png')

#imagen_rgb = 'figuras1.jpg' #input ('ruta de la imagen: ')
#imagen_bgr = cv2.imread(imagen_rgb)

#convertir imagen de BGR a HSV
imagen_hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)

#verde inicial
verde_inicial = np.array ([40, 50, 50])

#verde final
verde_final = np.array ([70, 255, 255])

#mascara de color verde
mascara = cv2.inRange (imagen_hsv, verde_inicial, verde_final)

tiempo_inicial = time.time()
momentos = cv2.moments (mascara)
x = momentos['m10'] / momentos['m00']
y = momentos['m01'] / momentos['m00']
area = momentos['m00']
tiempo_final = time.time()
print(x, ',', y, '-', area)
print(tiempo_final - tiempo_inicial)

tiempo_inicial = time.time()
datos_validos = np.ma.where(mascara==255)
cx = datos_validos[1].mean()
cy = datos_validos[0].mean()
carea = len(datos_validos[1])
tiempo_final = time.time()
print(cx, ',', cy, '-', area)
print(tiempo_final - tiempo_inicial)


cv2.imshow ('Imagen BGR', imagen_bgr)
cv2.imshow ('Imagen HSV', imagen_hsv)
cv2.imshow ('Imagen Mascara', mascara)


cv2.waitKey ()
cv2.destroyAllWindows ()