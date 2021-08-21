#Foreground Extraction in an image using Grabcut algorithm
import numpy as np
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('C:/Program Files/Python39/lena.png')
mask = np.zeros(image.shape[:2],np.uint8)
backgroundMode1 = np.zeros((1,65),np.float64)
foregroundMode1 = np.zeros((1,65),np.float64)
rectangle = (20,100,150,150)
cv2.grabCut(image,mask,rectangle,backgroundMode1,foregroundMode1,3,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
image=image*mask2[:,:,np.newaxis]
plt.imshow(image)
plt.colorbar()
plt.show()
