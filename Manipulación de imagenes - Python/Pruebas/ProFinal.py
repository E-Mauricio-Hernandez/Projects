import cv2
import numpy as np
import time

def nothing (x):
	pass

#camara web
#camara = cv2.VideoCapture (0)

#archivo .mov
camara = cv2.VideoCapture('video1.mov')

cv2.namedWindow ('Video')
'''
cv2.createTrackbar ('H min', 'Video', 0, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 54, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 34, 255, nothing)

cv2.createTrackbar ('H max', 'Video', 32, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)
'''
rojo_inicial = np.array([0, 54, 34])
rojo_final = np.array([32, 255, 255])
verde_inicial = np.array([30, 39, 31])
verde_final = np.array([82, 255, 255])

kernel = np.ones((3,3), np.uint8)
while True:
        ret, frame_bgr = camara.read ()
        frame_bgr = cv2.flip(cv2.transpose(frame_bgr), 0)
        #print(frame_bgr.shape)
        frame_bgr2 = (frame_bgr.copy()).astype(np.uint8)
        frame_bgr2 = frame_bgr[550:720, 0:1280]
        
        #print(frame_bgr.shape)
        if not ret:
                break;
                
        frame_bgr2 = ((frame_bgr2.astype(np.uint16))*0.2 - 4).astype(np.uint16)
        frame_bgr2[frame_bgr2 > 255] = 255 # [] todo valor mayor a 255 devuelve un true y luego afectada en el true le pone 255
        frame_bgr2[frame_bgr2 < 0] = 0
        frame_bgr2 = frame_bgr2.astype(np.uint8)
        
        #frame_bgr2 = cv2.dilate(frame_bgr2, kernel, iterations=2)
        frame_bgr2 = cv2.erode(frame_bgr2, kernel, iterations = 1)
        
        frame_hsv = cv2.cvtColor (frame_bgr2, cv2.COLOR_BGR2HSV)
        #frame_hsv = frame_hsv[550:720, 0:1280]

        #mascara de color verde
        mascara_roja = cv2.inRange (frame_hsv,rojo_inicial, rojo_final)
        mascara_verde = cv2.inRange (frame_hsv, verde_inicial, verde_final)

        momentos = cv2.moments(mascara_roja)
        #print (momentos)
        if momentos['m00'] != 0:
                x = int(momentos['m10'] / momentos['m00'])
                y = int(momentos['m01'] / momentos['m00'])
        else:
                continue
        #print(x, ',', y)

        cv2.circle(frame_bgr2, (x, y), 50, (103, 255, 0), 3)
        mascaraT = mascara_roja + mascara_verde
        #time.sleep(0.1)
        
        cv2.imshow ('Video', frame_bgr)
        #cv2.imshow ('HSV', frame_hsv)
        cv2.imshow ('Imagen Mascara', mascaraT)

        if cv2.waitKey (1) & 0xFF==ord('q'):
                break;

camara.release ()
cv2.destroyAllWindows ()

'''
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
'''
