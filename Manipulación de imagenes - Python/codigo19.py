import cv2

imagen_BGR = cv2.imread ('imagenes/figuras.jpg')
#imagen_BGR = cv2.imread ('imagenes/cam_ruido.png')
#imagen_BGR = cv2.imread ('lena_RGB.png')
imagen_GRIS = cv2.cvtColor(imagen_BGR, cv2.COLOR_BGR2GRAY)

suavizado = cv2.medianBlur(imagen_GRIS, 5)

ret, thresh0 = cv2.threshold(suavizado, 127, 255, cv2.THRESH_BINARY)

#imagen, maxValue, metodo adaptativo, tipo de umbralizado, tamaño del bloque, constante
thresh1 = cv2.adaptiveThreshold(suavizado, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

#imagen, maxValue, metodo adaptativo, tipo de umbralizado, tamaño del bloque, constante
thresh2 = cv2.adaptiveThreshold(suavizado, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

#imagen, thresh, maxValue, metodo adaptativo, tipo de umbralizado, tamaño del bloque, constante
ret3, thresh3 = cv2.threshold(suavizado, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

suavizado1 = cv2.GaussianBlur(imagen_GRIS, (5,5), 0)

#imagen, thresh, maxValue, metodo adaptativo, tipo de umbralizado, tamaño del bloque, constante
ret4, thresh4 = cv2.threshold(suavizado1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('imagen_BGR', imagen_BGR)
cv2.imshow('imagen_GRIS', imagen_GRIS)
#cv2.imshow('suavizado', suavizado)
cv2.imshow('thresh0', thresh0)
cv2.imshow('thresh1', thresh1)
cv2.imshow('thresh2', thresh2)
cv2.imshow('thresh3', thresh3)
cv2.imshow('thresh4', thresh4)


cv2.waitKey()
cv2.destroyAllWindows()