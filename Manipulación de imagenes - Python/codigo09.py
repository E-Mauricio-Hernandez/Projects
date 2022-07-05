import cv2
from time import time
import numpy as np


imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

#Primera forma
tiempo_inicial = time()
histograma = [0] * 256

#recorrer la imagen por filas
for f in range (0, imagen_GRIS.shape[0]):
	#recorrer la imagen por columnas
	for c in range (0, imagen_GRIS.shape[1]):
		histograma[imagen_GRIS[f, c]] = histograma[imagen_GRIS[f, c]] + 1

tiempo_final = time()
print('tiempo Primera Forma:', tiempo_final - tiempo_inicial)
#print(histograma)

#segunda forma
tiempo_inicial = time()
histograma1 = np.zeros((1, 256), np.uint16)

#recorrer la imagen por filas
for f in range (0, imagen_GRIS.shape[0]):
	#recorrer la imagen por columnas
	for c in range (0, imagen_GRIS.shape[1]):
		valor = imagen_GRIS.item (f, c)
		histograma1.itemset(0, valor, histograma1.item(0, valor) + 1)

tiempo_final = time()
print('tiempo Segunda Forma:', tiempo_final - tiempo_inicial)
#print(histograma1)

#tercera forma
tiempo_inicial = time()
histograma2 = [0] * 256

#recorrer la imagen por filas
for fila in imagen_GRIS:
	for pixel in fila:
		histograma2[pixel] = histograma2[pixel] + 1

tiempo_final = time()
print('tiempo tercera Forma:', tiempo_final - tiempo_inicial)
#print(histograma2)

cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)


cv2.waitKey()
cv2.destroyAllWindows()
