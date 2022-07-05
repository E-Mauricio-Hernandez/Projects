# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 17:43:55 2016

@author: diaz
"""
import cv2
import numpy as np


imagen = cv2.imread ('imagenes/dem.tif', cv2.IMREAD_UNCHANGED)
print ("tipo de dato;",imagen.dtype)
print ("dimensiones:", imagen.shape)
print ("minimo:",imagen.min())
print ("maximo:",imagen.max())

minimo = 0
maximo =5000

paleta = np.concatenate([
	np.zeros(minimo, dtype=np.uint16),
	np.linspace(0, 255, maximo - minimo).astype(np.uint16),
	np.ones(maximo, dtype=np.uint16)*255
	])

imagen_normalizada = paleta[imagen].astype(np.uint8)

cv2.imshow('imagen normalizada', cv2.applyColorMap(imagen_normalizada, cv2.COLORMAP_HOT))

#espera a que oprima una tecla para terminar
cv2.waitKey ()
#destruye la ventana creada
cv2.destroyAllWindows ()