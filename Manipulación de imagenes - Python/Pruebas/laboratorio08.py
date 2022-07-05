###Juan Esteban Velez hernandez - 161003641 #####
##laboratorio 08  Filtros
import cv2
import numpy as np
from time import time

imagen = input("Ingrese la ruta de la imagen: ");

imagen_BGR = cv2.imread (imagen)
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)
x = imagen_GRIS.shape[0]
y = imagen_GRIS.shape[1]
imagen_negra = imagen_GRIS.copy()
histogramagraf = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA1##
histogramagra2 = np.zeros((x, 256, 1),np.uint8)##GRAFICA_HISTOGRAMA2##

hist1 = cv2.calcHist([imagen_GRIS], [0], None, [256], [0, 256])##generar_histograma1


tamkernel = int(input("Ingrese la dimension del kernel: "));

kernel = np.zeros((tamkernel, tamkernel))
for pos0 in range(0, tamkernel):
	for pos01 in range(0, tamkernel):
		print("Ingrese el valor del Kernel en la posicion ","[",pos0,"]","[",pos01,"]")
		kernel[pos0][pos01] = int(input(" : "));

print("Kernel ingresado: ")
print(kernel)

kkernel = float(input("Ingrese la constante a dividir el kernel: "));

p = int((tamkernel - 1)/2)
limite1 = int(x - p)
limite2 = int(y - p)
acum = 0

tiempo_inicial = time()
kkernel = float(1/kkernel)
for pos in range(p, limite1):
	
	for pos1 in range(p, limite2):
		acum = 0
		for pos2 in range(0, tamkernel):
			te = int(pos2 - p)
			for pos3 in range(0, tamkernel):
				ta = int(pos3 - p)
				te = int(pos2 - p)
				acum = (kernel[pos3][pos2]*imagen_GRIS[pos + ta][pos1 + te])+ acum
		acum = acum*kkernel
		if (acum > 255):
			acum = 255
		if (acum < 0):	
			acum = 0
		
		imagen_negra[pos][pos1] = acum

hist2 = cv2.calcHist([imagen_negra], [0], None, [256], [0, 256])##generar_histograma2
##GRAFICAR HISTOGRAMA
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
#############NORMALIZAR IMAGEN RESULTANTE###############
for pos in range(0, 255):
	 hist2[pos]= hist2[pos]/n

#####GRAFICA HISTOGRAMA IMAGEN RESULTANTE############
for pos in range(0, x):
	for pos1 in range(0, 255):
		if pos <= hist2[pos1]:
			histogramagra2[-pos][pos1] = 255

tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

##GRAFICAR HISTOGRAMA
cv2.imshow('imagen_GRIS' , imagen_GRIS)	
cv2.imshow('imagen_resultante' , imagen_negra)
cv2.imshow('histograma1' , histogramagraf)
cv2.imshow('histograma_resultante' , histogramagra2)

cv2.waitKey()
cv2.destroyAllWindows()