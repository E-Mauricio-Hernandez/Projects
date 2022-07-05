import cv2
import numpy as np
import time


z1 = int(input('z1: '))
z2 = int(input('z2: '))

imagen_bgr = cv2.imread('imagenes/lena_RGB.png')
imagen_gris = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2GRAY)

tiempo_inicial = time.time()
imagen_resultado = imagen_gris.copy()
imagen_resultado[imagen_gris >= z2] = 255
imagen_resultado[imagen_gris <= z1] = 0
c = 255  / (z2 - z1)
imagen_resultado[(imagen_gris > z1) & (imagen_gris < z2)] = \
	imagen_resultado[(imagen_gris > z1) & (imagen_gris < z2)].astype(np.float16) * c

tiempo_final = time.time()
print(tiempo_final - tiempo_inicial)

cv2.imshow ('imagen_bgr', imagen_bgr)
cv2.imshow ('imagen_gris', imagen_gris)
cv2.imshow ('imagen_resultado', imagen_resultado)

cv2.waitKey ()
cv2.destroyAllWindows ()