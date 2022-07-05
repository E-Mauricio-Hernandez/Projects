import cv2
import numpy as np
import time

imagen_bgr = cv2.imread('lena_RGB.png')

tiempo_inicial = time.time()
print(imagen_bgr[100, 100])
operacion = imagen_bgr.astype(np.float16) - (100)
operacion[operacion > 255] = 255
operacion[operacion <0] = 0
print(operacion[100, 100])
tiempo_final = time.time()
print (tiempo_final - tiempo_inicial)

tiempo_inicial = time.time()
print(imagen_bgr[100, 100])
a = np.ones((imagen_bgr.shape[0], imagen_bgr.shape[1], imagen_bgr.shape[2]), dtype=np.uint8) * (10)
operacion1 = cv2.add (imagen_bgr, a)
print(operacion1[100, 100])
tiempo_final = time.time()
print (tiempo_final - tiempo_inicial)

cv2.imshow ('imagen_bgr', imagen_bgr)


cv2.waitKey ()
cv2.destroyAllWindows ()