###Juan Esteban Velez hernandez - 161003641 #####
##laboratorio 07  transformacion de la escala de niveles de grises

import cv2
import numpy as np
from time import time

imagen = input("Ingrese el nombre de la imagen: ");
z1 = float(input("Ingrese  z1 :" )); 
z2 = float(input("Ingrese  z2 :" )); 

imagen_BGR = cv2.imread (imagen)
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

x = imagen_GRIS.shape[0]
y = imagen_GRIS.shape[1]
imagen_negra= np.zeros((x, y, 1),np.uint8)##imagen_resultante
histogramagraf = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA1##
histogramagra2 = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA2##

hist1 = cv2.calcHist([imagen_GRIS], [0], None, [256], [0, 256])##generar_histograma1

tiempo_inicial = time()

for pos in range(0, x):
	for pos1 in range(0, y):
		if (imagen_GRIS[pos][pos1] >= z2):
			imagen_negra[pos][pos1] = 255
		if (imagen_GRIS[pos][pos1] <= z1):
			imagen_negra[pos][pos1] = 0
		if (z1 < imagen_GRIS[pos][pos1] < z2):
			imagen_negra[pos][pos1] = int((imagen_GRIS[pos][pos1]-z1)*255/(z2-z1))
			
hist2 = cv2.calcHist([imagen_negra], [0], None, [256], [0, 256])##generar_histograma2
	
#######n PARA IMAGEN ORIGINAL##############
maxs = max(hist1)
n = maxs/x	
#############NORMALIZAR IMAGEN ORIGINAL###############
for pos in range(0, 255):
	 hist1[pos]= hist1[pos]/n

#####GRAFICA HISTOGRAMA IMAGEN ORIGINAL############
for pos in range(0, x):
	for pos1 in range(0, 255):
		if pos <= hist1[pos1]:
			histogramagraf[-pos][pos1] = 255	

maxs = max(hist2)
n = maxs/x	
#############NORMALIZAR IMAGEN ecualizada###############
for pos in range(0, 255):
	 hist2[pos]= hist2[pos]/n

#####GRAFICA HISTOGRAMA IMAGEN ecualizada############
for pos in range(0, x):
	for pos1 in range(0, 255):
		if pos <= hist2[pos1]:
			histogramagra2[-pos][pos1] = 255

#cv2.imshow('imagen_BGR' , imagen_BGR)
cv2.imshow('imagen_GRIS' , imagen_GRIS)	
cv2.imshow('imagen_resultante' , imagen_negra)
cv2.imshow('histograma1' , histogramagraf)
cv2.imshow('histograma_resultante' , histogramagra2)

tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

cv2.waitKey()
cv2.destroyAllWindows()