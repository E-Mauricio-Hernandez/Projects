import cv2
import numpy as np

imagen = np.zeros((512, 512, 3), np.uint8)

imagen = cv2.line(imagen, (0, 0), (511, 511), (0, 0, 255), 5)

imagen = cv2.rectangle(imagen, (50, 50), (400, 400), (255, 0, 0), 5)

imagen = cv2.circle(imagen, (200, 200), 100, (0, 200, 200), -1)

cv2.imshow('Imagen', imagen)
cv2.waitKey()
cv2.destroyAllWindows()