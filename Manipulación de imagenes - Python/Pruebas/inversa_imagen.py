###Juan Esteban Velez hernandez - 161003641 #####
##ingresar nombre de la imagen Ejemplo : imagen.png
import cv2
from time import time

imagen = input("Ingrese el nombre del archivo para hallar la inversa de la imagen con el formato: ");
imagen_BGR = cv2.imread (imagen)
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)
imagen_GRIS_COPIA = imagen_GRIS.copy()

tiempo_inicial = time()

for pos in range(0, imagen_GRIS.shape[0]):
	for pos1 in range(0, imagen_GRIS.shape[1]):
		imagen_GRIS_COPIA[pos][pos1] = 255 - imagen_GRIS[pos][pos1]

cv2.imshow('imagen_BGR' , imagen_BGR)
#cv2.imshow('imagen_GRIS' , imagen_GRIS)	
cv2.imshow('imagen_INVERSA' , imagen_GRIS_COPIA)

tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

cv2.waitKey()
cv2.destroyAllWindows()