import cv2
import numpy as np
import time

imagen_bgr = cv2.imread('señalroja.png')
imagen_gris = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2GRAY)
imagen_contorno = np.ones((imagen_gris.shape[0], imagen_gris.shape[1]), dtype=np.uint8)
imagen_rectangulo_envolvente = np.ones((imagen_gris.shape[0], imagen_gris.shape[1]), dtype=np.uint8)

ret, umbralizacion = cv2.threshold(imagen_gris, 127, 255, 0)

imagen_contornos, contornos, jerarquia = cv2.findContours (umbralizacion, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
mayor_contorno = max(imagen_contornos, key = cv2.contourArea)

cv2.drawContours (imagen_contorno, contornos, 1, 255, 2)


contorno = contornos[186]
for i in range(0,len(contornos)):
	contorno = contornos[i]
	area = cv2.contourArea(contorno)

	print(area,i)
M = cv2.moments (contorno)
area = cv2.contourArea(contorno)
#area = M['m00']
#print(area)

area1 = cv2.contourArea (contorno)
print(area1)

perimetro = cv2.arcLength (contorno, True)
print(perimetro)

x, y, w, h = cv2.boundingRect(contorno)
cv2.rectangle (imagen_rectangulo_envolvente, (x, y), (x + w, y + h), 255, 2)

resultado = cv2.add (imagen_contorno, imagen_rectangulo_envolvente)


cv2.imshow ('imagen_bgr', imagen_bgr)
cv2.imshow ('imagen_gris', imagen_gris)
cv2.imshow ('umbralizacion', umbralizacion)
cv2.imshow ('imagen_contorno', imagen_contorno)
cv2.imshow ('imagen_rectangulo_envolvente', imagen_rectangulo_envolvente)
cv2.imshow ('resultado', resultado)



cv2.waitKey ()
cv2.destroyAllWindows ()