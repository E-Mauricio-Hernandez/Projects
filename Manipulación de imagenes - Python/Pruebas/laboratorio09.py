import cv2
import numpy as np
from time import time


imagen = input("Ingrese el DEM: ");
imagen = cv2.imread (imagen, cv2.IMREAD_UNCHANGED)
#imagen = cv2.imread ('dem.tif', cv2.IMREAD_UNCHANGED)

#opciones = [32,64,128,16,1,8,4,2]
#colores direccion de flujo
c1 = (255,0,255)
c2 = (255,0,0)
c3 = (255,215,0)
c4 = (0,0,255)	
c5 = (0,255,0)
c6 = (0,255,255)
c7 = (72,209,204)
c8 = (0,150,0)
opciones = [c1,c2,c3,c4,c5,c6,c7,c8]

#imagen = input("Ingrese la ruta de la imagen: ");
'''
print ("tipo de dato;",imagen.dtype)
print ("dimensiones:", imagen.shape)
print ("minimo:",imagen.min())
print ("maximo:",imagen.max())
'''
x = imagen.shape[0] - 1
y = imagen.shape[1] - 1
acum = 0

minimo = 0
maximo = 5000
#maximo = 1
##W es el tamaño del pixel del raster (en este caso 5 metros).
w = int(5)

paleta = np.concatenate([
	np.zeros(minimo, dtype=np.uint16),
	np.linspace(0, 255, maximo - minimo).astype(np.uint16),
	np.ones(maximo, dtype=np.uint16)*255
	])
imagen_normalizada = paleta[imagen].astype(np.uint8)

imagen_r1 = imagen_normalizada.copy()
imagen_r2 = imagen_normalizada.copy()
imagen_r3 = np.zeros(((x + 1), (y +1), 3),np.uint8)##imagen_resultante

for pos in range(1, x):
	for pos1 in range(1, y):
		##p, q, r, s, t son los parámetros iniciales para el cálculo de los atributos de flujo y forma.
		z1 = int(imagen_normalizada[pos - 1][pos1 - 1])
		z2 = int(imagen_normalizada[pos][pos1 - 1])
		z3 = int(imagen_normalizada[pos + 1][pos1 - 1])
		z4 = int(imagen_normalizada[pos - 1][pos1])
		z5 = int(imagen_normalizada[pos][pos1])
		z6 = int(imagen_normalizada[pos + 1][pos1])
		z7 = int(imagen_normalizada[pos - 1][pos1 + 1])
		z8 = int(imagen_normalizada[pos][pos1 + 1])
		z9 = int(imagen_normalizada[pos + 1][pos1 + 1])
		p = float((z3 + z6 + z9 - z1 - z4 -z7)/(6*w))
		q = float((z1 + z2 + z3 - z7 - z8 - z9)/(6*w))
		r = float((z1 + z3 + z4 + z6 + z7 + z9 -2*z2 -2*z5 -2*z8)/((3*w)**2))
		s = float((z3 + z7 - z1 - z9)/((4*w)**2))
		t = float((z1 + z2 + z3 + z7 + z8 + z9 -2*z4 -2*z5 -2*z6)/((3*w)**2))
		
		#Gaussian curvature (curvatura Gauseana) m-2 
		kv1 = (r*t) - (s**2)
		kv2 = (1 + (p**2) + (q**2))**2
		kv = kv1/kv2
		kv = kv*(2**16)

		imagen_r2[pos,pos1] = kv

		#Slope (pendiente), 0¶:  ##1
		G1 = float(p**2 + q**2)
		G = float(G1**(1/2))
		G = float((np.arctan(G1)))
		G = G *255

		imagen_r1[pos,pos1] = float(G)

		##direccion de flujo ##2
		kernel = [z1,z2,z3,z4,z6,z7,z8,z9]	
		acum = int(kernel[0])
		poss = 0
		for pos3 in range(0, 8):	
			if (acum < kernel[pos3]):
				acum = kernel[pos3]
				poss = pos3

		imagen_r3[pos,pos1] = opciones[poss]
		
#cv2.imshow('imagen normalizada', cv2.applyColorMap(imagen_r1, cv2.COLORMAP_JET))
cv2.imshow('imagen normalizada', imagen_normalizada)
cv2.imshow('imagen_resultante1 pendiente' , imagen_r1)
cv2.imshow('imagen_resultante2 curvatura gaussiana' , imagen_r2)
cv2.imshow('imagen_resultante3 direccion de flujo' , imagen_r3)
#cv2.imshow('imagen_resultante3' , cv2.applyColorMap(imagen_r1, cv2.COLORMAP_HOT))
#espera a que oprima una tecla para terminar
cv2.waitKey ()
#destruye la ventana creada
cv2.destroyAllWindows ()