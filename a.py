#Eroding an image
import cv2
import numpy as np
image = cv2.imread('C:/Program Files/Python39/cind.jpg')
image1 = cv2.imread('C:/Program Files/Python39/cind1.jpg')
window_name = 'Image'
Win_name = 'Image1'
kernel = np.ones((5,5),np.uint8)
image = cv2.erode(image,kernel)
Ker = np.ones((6,6),np.uint8)
image1 = cv2.erode(image1,Ker,cv2.BORDER_REFLECT)
cv2.imshow(window_name,image)
cv2.imshow(Win_name,image1)
#Blurring an image
image2 = cv2.imread('C:/Program Files/Python39/lena.png')
cv2.imshow('Original image',image2)
cv2.waitKey(0)
Gaussian = cv2.GaussianBlur(image2,(7,7),0)
cv2.imshow('Gaussian Blurring',Gaussian)
cv2.waitKey(0)
median = cv2.medianBlur(image2,5)
cv2.imshow('Median Blurring',median)
cv2.waitKey(0)
bilateral=cv2.bilateralFilter(image2,9,75,75)
cv2.imshow('Bilateral Blurring',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Creating border around images
image4=cv2.imread('C:/Program Files/Python39/lena.png')
wind_name='Image4'
image4 = cv2.copyMakeBorder(image4,10,10,10,10,cv2.BORDER_CONSTANT)
cv2.imshow(wind_name,image4)
windo_name='Imag'
image4 = cv2.copyMakeBorder(image4,100,100,50,50,cv2.BORDER_REFLECT)
cv2.imshow(windo_name,image4)
#Grayscaling of images
image5=cv2.imread('C:/Program Files/Python39/lena.png',0)
window_nam = 'Image5'
cv2.imshow(window_nam,image5)
cv2.imshow('Original',image4)
cv2.waitKey()
gray_image=cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray scale',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


    
    
    
    



