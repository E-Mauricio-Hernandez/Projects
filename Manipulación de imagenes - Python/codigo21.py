import cv2
import numpy as np
from time import time

#imagen_BGR = cv2.imread ('imagenes/lena_RGB.png')
#imagen_BGR = cv2.imread ('imagenes/figuras1.png')
#imagen_BGR = cv2.imread ('imagenes/monedas.png')
#imagen_BGR = cv2.imread ('imagenes/mano1.png')
#imagen_BGR = cv2.imread ('imagenes/cam_ruido.png')
imagen_BGR = cv2.imread ('imagenes/ruido5.png')
#imagen_BGR = cv2.imread ('imagenes/ruido4.png')
#imagen_BGR = cv2.imread ('imagenes/ruido2.jpg')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

kernel = np.ones((3, 3), np.uint8)

erosion = cv2.erode(imagen_GRIS, kernel, iterations=1)

dilatacion = cv2.dilate(imagen_GRIS, kernel, iterations=1)

gradiente = dilatacion - erosion

apertura = cv2.morphologyEx(imagen_GRIS, cv2.MORPH_OPEN, kernel)

cierre = cv2.morphologyEx(imagen_GRIS, cv2.MORPH_CLOSE, kernel)

tophat = cv2.morphologyEx(imagen_GRIS, cv2.MORPH_TOPHAT, kernel)

blackhat = cv2.morphologyEx(imagen_GRIS, cv2.MORPH_BLACKHAT, kernel)

suavizado = cv2.GaussianBlur(imagen_GRIS, (3,3), 0)

ret1, th1 = cv2.threshold(suavizado, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

ruido = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)

erosion1 = cv2.erode(ruido, kernel, iterations=1)

dilatacion1 = cv2.dilate(ruido, kernel, iterations=1)

gradiente1 = dilatacion1 - erosion1


cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('erosion', erosion)
cv2.imshow('dilatacion', dilatacion)
cv2.imshow('gradiente', gradiente)
cv2.imshow('apertura', apertura)
cv2.imshow('cierre', cierre)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.imshow('suavizado', suavizado)
cv2.imshow('th1', th1)
cv2.imshow('ruido', ruido)
cv2.imshow('gradiente1', gradiente1)



cv2.waitKey()
cv2.destroyAllWindows()
