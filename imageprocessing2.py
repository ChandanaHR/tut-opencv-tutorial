import cv2
import numpy as np
#scaling operation
try:
    image1 = cv2.imread('C:/Program Files/Python39/lena.png')
    #getting number of pixels
    (height,width)=image1.shape[:2]
    res = cv2.resize(image1,(int(width/2),int(height/2)),interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Result image1',res)
except IOError:
    print('Error while reading files!!!')
#Rotating operation
try:
    image2 = cv2.imread('C:/Program Files/Python39/lena.png')
    (rows,cols) = image2.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
    result = cv2.warpAffine(image2,M,(cols,rows))
    cv2.imshow('Result image2',result)
except IOError:
    print('Error while reading files!!!')
#Translating images
N = np.float32([[1,0,100],[0,1,50]])
try:
    image3 = cv2.imread('C:/Program Files/Python39/lena.png')
    (rows,cols) = image3.shape[:2]
    result1 = cv2.warpAffine(image3,N,(cols,rows))
    cv2.imshow('Result image3',result1)
except IOError:
    print('Error while reading files!!!')
#Edge Detection
try:
    image4 = cv2.imread('C:/Program Files/Python39/lena.png')
    #Canny edge detection
    edges = cv2.Canny(image4,200,400)
    cv2.imshow('Result image4',edges)
except IOError:
    print('Error while reading files!!!')


