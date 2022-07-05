import cv2
from time import time
import numpy as np

imagen_BGR = cv2.imread ('lena_RGB.png')



print(imagen_BGR[100, 200])
print(imagen_BGR[100] [200])

imagen_BGR[100, 200] = [0, 255, 0]
print(imagen_BGR[100, 200])

print(imagen_BGR.shape)
print(imagen_BGR.size)
print(imagen_BGR.dtype)

tiempo_inicial = time()
b, g, r = cv2.split(imagen_BGR)
tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

tiempo_inicial = time()
b1 = imagen_BGR[:, :, 0] 
g1 = imagen_BGR[:, :, 1] 
r1 = imagen_BGR[:, :, 2]
tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)

cv2.imshow('b1', b1)
cv2.imshow('g1', g1)
cv2.imshow('r1', r1)

tiempo_inicial = time()
imagen_BGR_union = cv2.merge ((b, g, r))
tiempo_final = time()
print('tiempo:', tiempo_final - tiempo_inicial)
cv2.imshow('imagen_BGR_union', imagen_BGR_union)



tiempo_inicial = time()
imagen_BGR_union1 = imagen_BGR.copy()
imagen_BGR_union1[:, :, 0] = b1
imagen_BGR_union1[:, :, 1] = g1
imagen_BGR_union1[:, :, 2] = r1
tiempo_final = time()
print('tiempo union1:', tiempo_final - tiempo_inicial)
cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_BGR_union1', imagen_BGR_union1)

tiempo_inicial = time()
imagen_BGR_union2 = np.dstack((b1, g1, r1))
tiempo_final = time()
print('tiempo union2:', tiempo_final - tiempo_inicial)

#imagen_BGR[:, :, 1] = 0
#imagen_BGR[:, :, 2] = 0

tiempo_inicial = time()
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)
tiempo_final = time()
print('tiempo gris1:', tiempo_final - tiempo_inicial)

tiempo_inicial = time()
imagen_GRIS1 = np.uint8(((np.float16(imagen_BGR[:, :, 0])*0.114) + (np.float16(imagen_BGR[:, :, 1])*0.587) + (np.float16(imagen_BGR[:, :, 2]))*0.299))
tiempo_final = time()
print('tiempo gris2:', tiempo_final - tiempo_inicial)

cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_BGR_union1', imagen_BGR_union1)
cv2.imshow('imagen_BGR_union2', imagen_BGR_union2)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('imagen_GRIS1', imagen_GRIS1)

cv2.waitKey()
cv2.destroyAllWindows()
