import cv2
import numpy as np

#capturar imagen
imagen_rgb = input ('ruta de la imagen: ')
imagen_bgr = cv2.imread(imagen_rgb)

#convertir imagen de BGR a HSV
imagen_hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)

#verde inicial
verde_inicial = np.array ([40, 50, 50])

#verde final
verde_final = np.array ([70, 255, 255])

#mascara de color verde
mascara = cv2.inRange (imagen_hsv, verde_inicial, verde_final)

print(imagen_bgr[100, 100])
print(imagen_hsv[100, 100])


cv2.imshow ('Imagen BGR', imagen_bgr)
cv2.imshow ('Imagen HSV', imagen_hsv)
cv2.imshow ('Imagen Mascara', mascara)


cv2.waitKey ()
cv2.destroyAllWindows ()