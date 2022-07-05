import cv2

camara = cv2.VideoCapture(0)

while True:
	ret, frame = camara.read()
	cv2.imshow('Video', frame)
	if cv2.waitKey (1) & 0xFF == ord ('q'):
		break