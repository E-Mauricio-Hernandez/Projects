###Juan Esteban Velez hernandez - 161003641 #####
##ingresar nombre de la imagen con su extension Ejemplo : imagen.png
import cv2
from time import time
import numpy as np

imagen = input("Ingrese el nombre el nombre de la imagen con su extension: ");
imagen_BGR = cv2.imread (imagen)
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)##imagen en escala de grises

m = 0
x = imagen_GRIS.shape[0]
y = imagen_GRIS.shape[1]
histogramagraf = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA##

cv2.imshow('imagen_BGR' , imagen_BGR)
cv2.imshow('imagen_GRIS' , imagen_GRIS)

tiempo_inicial = time()
################GENERAR_HISTOGRAMA##############
ma = cv2.calcHist([imagen_GRIS], [0], None, [256], [0, 256])##generar histograma
#for pos in range(0, x):
	#for pos1 in range(0, y):
		#m = imagen_GRIS[pos][pos1]
		#ma[m] +=1
#print('vector histograma',ma) 

#######n##############
maxs = max(ma)
n = maxs/x	
#############NORMALIZAR###############
for pos in range(0, 255):
	 ma[pos]= ma[pos]/n
#print('vector histograma normalizado',ma) 

#####GRAFICA HISTOGRAMA############
for pos in range(0, x):
	for pos1 in range(0, 255):
		#hc = ma[pos1]
		if pos <= ma[pos1]:
			histogramagraf[-pos][pos1] = 255

tiempo_final = time()
print('tiempo', tiempo_final - tiempo_inicial)
cv2.imshow('Histograma',histogramagraf)	
cv2.waitKey()
cv2.destroyAllWindows()

#histograma3 = [0] * 256 vector de 256 posiciones
##########################################################