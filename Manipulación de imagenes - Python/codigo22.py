import cv2
import numpy as np
from time import time

imagen_BGR = cv2.imread ('lena_RGB.png')
#imagen_BGR = cv2.imread ('imagenes/figuras1.png')
#imagen_BGR = cv2.imread ('imagenes/monedas.png')
#imagen_BGR = cv2.imread ('imagenes/mano1.png')
#imagen_BGR = cv2.imread ('imagenes/cam_ruido.png')
#imagen_BGR = cv2.imread ('imagenes/ruido4.png')
#imagen_BGR = cv2.imread ('imagenes/ruido2.jpg')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(imagen_GRIS, 100, 200, 3)

gausiana = cv2.GaussianBlur(imagen_GRIS, (3, 3), 0)

canny1 = cv2.Canny(gausiana, 100, 200, 3)


cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('canny', canny)
cv2.imshow('gausiana', gausiana)
cv2.imshow('canny1', canny1)




cv2.waitKey()
cv2.destroyAllWindows()
