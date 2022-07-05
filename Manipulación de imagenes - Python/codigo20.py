import cv2
import numpy as np
from time import time

imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)
suavizado = cv2.GaussianBlur(imagen_GRIS, (3,3), 0)
ret, thresh = cv2.threshold(suavizado, 127, 255, cv2.THRESH_BINARY)



tiempo_inicial = time()
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations = 1)
tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

binario = thresh / 255
erosion1 = thresh.copy()

tiempo_inicial = time()
kernel = np.ones((3, 3), np.uint8)

for f in range(1, thresh.shape[0] - 1):
	for c in range(1, thresh.shape[1] - 1):
		suma = binario[f-1, c-1] + binario[f-1, c] + binario[f-1, c+1] + binario[f, c-1] + binario[f, c] + binario[f, c+1] + binario[f+1, c-1] + binario[f+1, c] + binario[f+1, c+1]
		if int(suma)==int(kernel.size):
			erosion1[f, c] = 255
		else:
			erosion1[f, c] = 0

tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

binario = thresh / 255
erosion2 = thresh.copy()

tiempo_inicial = time()
kernel = np.ones((3, 3), np.uint8)

for f in range(1, thresh.shape[0] - 1):
	for c in range(1, thresh.shape[1] - 1):
		if binario[f-1:f+2, c-1:c+2].all() == kernel.all():
			erosion2[f,c] = 255
		else:
			erosion2[f,c] = 0
			
tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)


cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('thresh', thresh)
cv2.imshow('erosion', erosion)
cv2.imshow('erosion1', erosion1)
cv2.imshow('erosion2', erosion2)

cv2.waitKey()
cv2.destroyAllWindows()
