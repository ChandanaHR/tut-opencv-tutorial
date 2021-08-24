#Morphological operation on images
import cv2
import numpy as np
screenRead = cv2.VideoCapture(0)
while(1):
    _, image = screenRead.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    blue1 = np.array([110,50,50])
    blue2 = np.array([130,255,255])
    mask = cv2.inRange(hsv,blue1,blue2)
    res = cv2.bitwise_and(image,image,mask=mask)
    kernel = np.ones((5,5),np.uint8)
    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    cv2.imshow('Mask',mask)
    cv2.imshow('Opening',opening)
    if cv2.waitKey(1) & 0xff == ord('a'):
        break
cv2.destroyAllWindows()
screenRead.release()
