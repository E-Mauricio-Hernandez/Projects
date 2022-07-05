import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)

imagen_bgr = cv2.imread('prubeaazul2.png')
cv2.namedWindow ('Video')
cv2.createTrackbar ('H min', 'Video', 107, 180, nothing)
cv2.createTrackbar ('S min', 'Video', 121, 255, nothing)
cv2.createTrackbar ('V min', 'Video', 75, 255, nothing)
cv2.createTrackbar ('H max', 'Video', 110, 180, nothing)
cv2.createTrackbar ('S max', 'Video', 255, 255, nothing)
cv2.createTrackbar ('V max', 'Video', 255, 255, nothing)

kernel = np.ones((3,3),np.uint8)

imagen_bgr = imagen_bgr[100:440, 140:1050]

while(1):
    #imagen_bgr = cv2.flip(cv2.transpose(imagen_bgr), 1)
    #imagen_bgr = imagen_bgr[180:500, 0:]
    hsv = cv2.cvtColor (imagen_bgr, cv2.COLOR_BGR2HSV)

    #mask = cv2.inRange (hsv, np.array ([Hmin, Smin, Vmin]), np.array ([Hmax, Smax, Vmax]))
    mask = cv2.inRange (hsv, 
        np.array ([cv2.getTrackbarPos ('H min', 'Video'), cv2.getTrackbarPos ('S min', 'Video'), cv2.getTrackbarPos ('V min', 'Video')]),
        np.array ([cv2.getTrackbarPos ('H max', 'Video'), cv2.getTrackbarPos ('S max', 'Video'), cv2.getTrackbarPos ('V max', 'Video')]))
    #mascara_rojo1 = cv2.inRange(hsv, rojo_bajos1, rojo_altos1)
    #mask = cv2.bitwise_and(imagen_bgr,imagen_bgr, mask= mask)
    mask = cv2.dilate (mask, cv2.getStructuringElement (cv2.MORPH_RECT, (5, 5)), iterations = 1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)


    Hmin = cv2.getTrackbarPos ('H min', 'Video')
    Smin = cv2.getTrackbarPos ('S min', 'Video')
    Vmin = cv2.getTrackbarPos ('V min', 'Video')
    Hmax = cv2.getTrackbarPos ('H max', 'Video')
    Smax = cv2.getTrackbarPos ('S max', 'Video')
    Vmax = cv2.getTrackbarPos ('V max', 'Video')
    cv2.imshow('imagen',imagen_bgr)
    #cv2.imshow ('hsv', hsv)

    cv2.imshow ('Video', mask)



    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()