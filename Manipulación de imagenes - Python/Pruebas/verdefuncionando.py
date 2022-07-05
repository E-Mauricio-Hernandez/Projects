import cv2
import numpy as np
#from time import time

#def nothing (x):
#	pass

video = input("Ingrese la ruta del video: ");
girar = int(input("Girar video , si 1, no 0: "));

camara = cv2.VideoCapture (video) 
		##27 mover
#camara = cv2.VideoCapture ('VIDEOS/video35.mov') ##29  ##32  ##señal verde 33  27 35

##señal amarilla 6  20
##señal roja  32
cv2.namedWindow ('Video')

#Rojos:
rojo_bajos1 = np.array([0,117,75], dtype=np.uint8) #3,65,75
rojo_altos1 = np.array([3, 196, 255], dtype=np.uint8) #12, 255, 255
rojo_bajos2 = np.array([240,65,75], dtype=np.uint8)
rojo_altos2 = np.array([256, 255, 255], dtype=np.uint8)

#Nuevos verdes:
verdes_bajos = np.array ([79, 82, 82])
verdes_altos = np.array ([86, 220, 220])# 90 primer term

#Amarillos:
amarillo_bajos = np.array ([19, 165, 100]) #167 2 term    
amarillo_altos = np.array ([30, 255, 255])

#Naranjas
naranja_bajos = np.array([10,190,138], dtype=np.uint8)   #9,100,138
naranja_altos = np.array([13, 255, 255], dtype=np.uint8)

#Azules:
azul_bajos = np.array([108,140,75], dtype=np.uint8)    #109 65  105,109,75
azul_altos = np.array([110, 198, 255], dtype=np.uint8)   # 107, 255, 255

kernel = np.ones((3,3),np.uint8)
while True:
	ret, frame_bgr = camara.read ()
	if not ret:
		break;

	frame_bgr = cv2.flip(cv2.transpose(frame_bgr), girar)
	frame_original = frame_bgr
	frame_bgr = frame_bgr[120:440, 180:1060]  #2 valor 500  

	hsv = cv2.cvtColor (frame_bgr, cv2.COLOR_BGR2HSV)

	#mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
	#mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	#mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	#mask = cv2.add(mascara_rojo1, mascara_rojo2)
	#Mascaras 
	mask_verde = cv2.inRange(hsv, verdes_bajos, verdes_altos)
	mask_amarillo = cv2.inRange(hsv, amarillo_bajos, amarillo_altos)
	mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
	mascara_rojo2 = cv2.inRange(hsv, rojo_bajos2, rojo_altos2)
	mask_roja = cv2.add(mascara_rojo1, mascara_rojo2)
	mask_naranja = cv2.inRange(hsv, naranja_bajos, naranja_altos)
	mask_azul = cv2.inRange(hsv, azul_bajos, azul_altos)


	#Filtros verdes
	mask_verde = cv2.dilate (mask_verde, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask_verde = cv2.morphologyEx(mask_verde, cv2.MORPH_OPEN, kernel)
	mask_verde = cv2.morphologyEx(mask_verde, cv2.MORPH_CLOSE, kernel)
	#mask_verde = cv2.GaussianBlur(mask_verde,(5,5),0)
	#Filtros amarillos
	mask_amarillo = cv2.dilate (mask_amarillo, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask_amarillo = cv2.morphologyEx(mask_amarillo, cv2.MORPH_OPEN, kernel)
	mask_amarillo = cv2.morphologyEx(mask_amarillo, cv2.MORPH_CLOSE, kernel)
	#Filtros rojos
	mask_roja = cv2.dilate (mask_roja, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask_roja = cv2.morphologyEx(mask_roja, cv2.MORPH_OPEN, kernel)
	mask_roja = cv2.morphologyEx(mask_roja, cv2.MORPH_CLOSE, kernel)
	#mask_roja = cv2.Canny(mask_roja, 100, 200, 3)

	#Filtros naranjas
	mask_naranja = cv2.dilate (mask_naranja, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask_naranja = cv2.morphologyEx(mask_naranja, cv2.MORPH_OPEN, kernel)
	mask_naranja = cv2.morphologyEx(mask_naranja, cv2.MORPH_CLOSE, kernel)

	#Filtros AZUL
	mask_azul = cv2.dilate (mask_azul, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
	mask_azul = cv2.morphologyEx(mask_azul, cv2.MORPH_OPEN, kernel)
	mask_azul = cv2.morphologyEx(mask_azul, cv2.MORPH_CLOSE, kernel)
	#mask = cv2.erode (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (3, 3)), iterations = 1)
	#mask = cv2.Canny(mask, 100, 200, 3)

	#Detectamos contornos, nos quedamos con el mayor y calculamos su centro
	#Contorno verde
	_, contours_verde, hierarchy = cv2.findContours(mask_verde, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#Condicion de contornos VERDE
	if len(contours_verde) == 0:
		mayor_contorno_verde = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno_verde = max(contours_verde, key = cv2.contourArea)

	#Contorno amarillo
	_, contours_amarillo, hierarchy = cv2.findContours(mask_amarillo, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#Condicion de contornos AMARILLO
	if len(contours_amarillo) == 0:
		mayor_contorno_amarillo = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno_amarillo = max(contours_amarillo, key = cv2.contourArea)

	#Contorno rojo
	_, contours_rojo, hierarchy = cv2.findContours(mask_roja, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#Condicion de contornos ROJA
	if len(contours_rojo) == 0:
		mayor_contorno_rojo = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno_rojo = max(contours_rojo, key = cv2.contourArea)

	#Contorno naranja
	_, contours_naranja, hierarchy = cv2.findContours(mask_naranja, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#Condicion de contornos NARANJA
	if len(contours_naranja) == 0:
		mayor_contorno_naranja = 1
	else:
		mayor_contorno_naranja = max(contours_naranja, key = cv2.contourArea)

	#Contorno AZUL
	_, contours_azul, hierarchy = cv2.findContours(mask_azul, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#Condicion de contornos VERDE
	if len(contours_azul) == 0:
		mayor_contorno_azul = 1
		#mayor_contorno=max(contours, key = cv2.contourArea)
	else:
		mayor_contorno_azul = max(contours_azul, key = cv2.contourArea)

	#Momento verdes
	momentos_verde = cv2.moments(mayor_contorno_verde)
	cx = int(momentos_verde['m10']/momentos_verde['m00'])
	cy = int(momentos_verde['m01']/momentos_verde['m00'])
	#Momento amarillos
	momentos_amarillo = cv2.moments(mayor_contorno_amarillo)
	cx1 = int(momentos_amarillo['m10']/momentos_amarillo['m00'])
	cy1 = int(momentos_amarillo['m01']/momentos_amarillo['m00'])
	#Momento ROJOS
	momentos_rojo = cv2.moments(mayor_contorno_rojo)
	cx2 = int(momentos_rojo['m10']/momentos_rojo['m00'])
	cy2 = int(momentos_rojo['m01']/momentos_rojo['m00'])
	#Momento naranja
	momentos_naranja = cv2.moments(mayor_contorno_naranja)
	cx2 = int(momentos_naranja['m10']/momentos_naranja['m00'])
	cy2 = int(momentos_naranja['m01']/momentos_naranja['m00'])

	#Momento naranja
	momentos_azul = cv2.moments(mayor_contorno_azul)
	cx2 = int(momentos_azul['m10']/momentos_azul['m00'])
	cy2 = int(momentos_azul['m01']/momentos_azul['m00'])
	# el momento 00 retorna el área
	#Area verde
	area_verde = momentos_verde ['m00']
	#Area amarilla
	area_amarillo = momentos_amarillo ['m00']
	#Area roja
	area_roja = momentos_rojo ['m00']
	#Area naranja
	area_naranja = momentos_naranja ['m00']
	#Area azul
	area_azul = momentos_azul ['m00']
	# imprimimos el área
	#print ('area:', area)	
	#Pregunta area para VERDE
	if 1200 < area_verde < 12000 : # 6000
		#if area_verde < 12000: # 12000
		approx = cv2.approxPolyDP(mayor_contorno_verde,0.05*cv2.arcLength(mayor_contorno_verde,True),True)
		if len(approx) == 4:
			#print(len(approx))
			cx = int(momentos_verde['m10']/momentos_verde['m00'])
			cy = int(momentos_verde['m01']/momentos_verde['m00'])
			cv2.circle (frame_bgr, (cx, cy), 30, (0, 255, 0), 2)
			print("señal verde de destino")
	#Pregunta area para AMARILLO
	if area_amarillo > 2000:   #1900   #2700		#Ultimo 2000
		if area_amarillo < 3050: #3000
			approx = cv2.approxPolyDP(mayor_contorno_amarillo,0.05*cv2.arcLength(mayor_contorno_amarillo,True),True)
			if len(approx) == 5:
				cx = int(momentos_amarillo['m10']/momentos_amarillo['m00'])
				cy = int(momentos_amarillo['m01']/momentos_amarillo['m00'])
				cv2.circle (frame_bgr, (cx, cy), 30, (255, 255, 0), 2)
				print("señal amarilla advertencia")
	#Pregunta area para ROJO
	if area_roja > 1900: #6000  ##3400
		if area_roja < 8000:
			approx = cv2.approxPolyDP(mayor_contorno_rojo,0.05*cv2.arcLength(mayor_contorno_rojo,True),True)
			if len(approx) == 6:
				#print(len(approx))
				cx = int(momentos_rojo['m10']/momentos_rojo['m00'])
				cy = int(momentos_rojo['m01']/momentos_rojo['m00'])
				cv2.circle (frame_bgr, (cx, cy), 30, (0, 0, 255), 2)
				print("señal roja cuidado")
	#Pregunta area para naranja
	if area_naranja > 1000:
		if area_naranja < 6881:
			approx = cv2.approxPolyDP(mayor_contorno_naranja,0.05*cv2.arcLength(mayor_contorno_naranja,True),True)
			if len(approx) == 4:
				cx = int(momentos_naranja['m10']/momentos_naranja['m00'])
				cy = int(momentos_naranja['m01']/momentos_naranja['m00'])
				cv2.circle (frame_bgr, (cx, cy), 30, (255, 128, 0), 2)
				print("señal naranja de desvio")
	#Pregunta area para naranja
			
	if 1100 < area_azul < 1300 or 3000 < area_azul < 4000 : # 6000
		approx = cv2.approxPolyDP(mayor_contorno_azul,0.05*cv2.arcLength(mayor_contorno_azul,True),True)
		if len(approx) == 4:
			#print("vertices")
			#print(len(approx))
			cx = int(momentos_azul['m10']/momentos_azul['m00'])
			cy = int(momentos_azul['m01']/momentos_azul['m00'])
			cv2.circle (frame_bgr, (cx, cy), 30, (255, 0, 0), 2)
			print("señal azul de servicios")
			#print(area_azul)
	cv2.imshow ('frame_bgr', frame_bgr)
	#cv2.imshow ('frame_hsv', hsv)
	#cv2.imshow ('mascara', mask_verde)
	#cv2.imshow ('mascara',  mask_amarillo)

	#cv2.imshow ('res', resultado)

	#cv2.imshow ('frame_roi', frame_roi)


	if cv2.waitKey (10) & 0xFF==ord('q'):
		break;

camara.release ()
cv2.destroyAllWindows ()