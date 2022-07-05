import cv2
import numpy as np

imagen_dem = cv2.imread('tif/dem.tif', cv2.IMREAD_UNCHANGED)

print(imagen_dem.dtype)
print(imagen_dem.shape)
print(imagen_dem.min())
print(imagen_dem.max())

minimo = 0
maximo = 5000

paleta = np.concatenate(
	[
	np.zeros(minimo, dtype=np.uint16),
	np.linspace(0, 255, maximo - minimo).astype(np.uint16),
	np.ones(5000 - maximo, dtype=np.uint16) * 255
	])

imagen_normalizada = paleta[imagen_dem].astype(np.uint8)


cv2.imshow('imagen normalizada', 
	cv2.applyColorMap(imagen_normalizada, cv2.COLORMAP_RAINBOW))
cv2.waitKey()
cv2.destroyAllWindows()