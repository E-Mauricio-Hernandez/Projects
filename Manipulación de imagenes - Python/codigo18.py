import cv2
import numpy as np

imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

ret,thresh1 = cv2.threshold(imagen_GRIS, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('thresh1', thresh1)


cv2.waitKey()
cv2.destroyAllWindows()
