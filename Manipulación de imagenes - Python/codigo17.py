import cv2
import numpy as np

imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

umbral = 127

imagen_umbral = np.ones(imagen_GRIS.shape, np.uint8)

mascara = imagen_GRIS >= umbral
print(imagen_GRIS)
print(mascara)
imagen_umbral = imagen_umbral * mascara * 255
print(imagen_umbral.dtype)

cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
cv2.imshow('imagen_umbral', imagen_umbral)


cv2.waitKey()
cv2.destroyAllWindows()
