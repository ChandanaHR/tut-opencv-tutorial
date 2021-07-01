#Converting from one color space to another
import cv2
import numpy as np
image=cv2.imread('C:/Program Files/Python39/lena.png')
window_name='Image'
image1 = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow(window_name,image1)
#We can also convert to grayscale just by placing 0 in front of path of image

#HSV color space.HSV colorspace is used for object tracking
window_name='Image2'
image2=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow(window_name,image2)

#Denoising of colored images using opencv
from matplotlib import pyplot as plt
dest=cv2.fastNlMeansDenoisingColored(image,None,10,10,7,15)
plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image)
plt.show()

#Visualizing images in different color spaces
#python program to read image as RGB
image3=cv2.imread('C:/Program Files/Python39/lena.png')
plt.imshow(image3)
plt.show()

#YCrCb color space
image4=cv2.cvtColor(image3,cv2.COLOR_BGR2YCrCb)
cv2.imshow('Image3',image4)

#HSV color space
image5=cv2.cvtColor(image3,cv2.COLOR_BGR2HSV)
cv2.imshow('Image4',image5)

#LAB color space
image6=cv2.cvtColor(image3,cv2.COLOR_BGR2LAB)
cv2.imshow('Image5',image6)

#edge map of image
laplacian=cv2.Laplacian(image3,cv2.CV_64F)
cv2.imshow('Image6',laplacian)

#heat map of image
plt.imshow(image3,cmap='hot')

#spectral image map
plt.imshow(image3,cmap='nipy_spectral')
