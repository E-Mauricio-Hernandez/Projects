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
print('histograma', histograma)

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

#cuarta forma
tiempo_inicial = time()
histograma3 = [0] * 256

for intensidad in range(0, 256):
	histograma3[intensidad] = len(imagen_GRIS[(imagen_GRIS==intensidad)])

tiempo_final = time()
print('tiempo cuarta Forma:', tiempo_final - tiempo_inicial)
#print(histograma3)

#quinta forma
tiempo_inicial = time()
histograma4 = cv2.calcHist([imagen_GRIS], [0], None, [256], [0, 256])
tiempo_final = time()
print('tiempo quinta forma:', tiempo_final - tiempo_inicial)
#print(histograma4)

#sexta forma
tiempo_inicial = time()
histograma5, bins = np.histogram(imagen_GRIS.ravel(),256,[0,256])
tiempo_final = time()
print('tiempo sexta forma:', tiempo_final - tiempo_inicial)
#print(histograma5)


#septima forma
#tiempo_inicial = time()
#histograma6 = [0] * 256
#imagen_GRIS_lista = imagen_GRIS.tolist()
#print(imagen_GRIS_lista)
#msk = [(el==100) for el in imagen_GRIS_lista]
#print(imagen_GRIS_lista)
#print(msk)
#array = np.array(imagen_GRIS)
#mascara = np.ma.masked_where(imagen_GRIS==100, imagen_GRIS)
#print(list(mascara))
#print(len(np.ma.compressed(mascara)))
#a = np.arange(4)

#print((np.ma.masked_where(imagen_GRIS!=100, imagen_GRIS)))
#for intensidad in range(0, 256):
	#histograma6[intensidad] = np.ma.compressed(np.ma.masked_where(imagen_GRIS==intensidad, imagen_GRIS))

#tiempo_final = time()
#print('tiempo septima Forma:', tiempo_final - tiempo_inicial)
#print(histograma6)


cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)


cv2.waitKey()
cv2.destroyAllWindows()
