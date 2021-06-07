#In order to separate the colors of image
import cv2
import numpy as np
img = cv2.imread('C:/Program Files/Python39/lena.png')
B,G,R = cv2.split(img)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.imshow("Blue",B)
cv2.waitKey(0)
cv2.imshow("Green",G)
cv2.waitKey(0)
cv2.imshow("Red",R)
cv2.waitKey(0)
cv2.destroyAllWindows()
