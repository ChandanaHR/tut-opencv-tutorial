import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('C:/Program Files/Python39/lena.png',0)
plt.hist(image.ravel(),bins=256,range=(0.0,1.0),fc='k',ec='k')
plt.show()
#Histogram calculation
histg = cv2.calcHist([image],[0],None,[256],[0,256])
plt.plot(histg)
plt.show()
#Histogram equalization
equ = cv2.equalizeHist(image)
res = np.hstack((image,equ))
cv2.imshow('Image',res)
#Simple thresholding of image
ret,thresh1 = cv2.threshold(image,120,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(image,120,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(image,120,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(image,120,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(image,120,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('Binary threshold',thresh1)
cv2.imshow('Binary threshold inverted',thresh2)
cv2.imshow('threshold trunc',thresh3)
cv2.imshow('threshold tozero',thresh4)
cv2.imshow('threshold tozero inv',thresh5)
#Adaptive thresholding
thresh6 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
thresh7 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)
cv2.imshow('Adaptive mean',thresh6)
cv2.imshow('Adaptive Gaussian',thresh7)
#Otsu thresholding
ret,thresh8 = cv2.threshold(image,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('otsu threshold',thresh8)
if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()



