#Arithmetic operations on images
import cv2
import numpy as np
image1 = cv2.imread('C:/Program Files/Python39/crop.jfif')
image2 = cv2.imread('C:/Program Files/Python39/cind1.jpg')
weightedsum = cv2.addWeighted(image1,0.5,image2,0.4,0)   #Addition
cv2.imshow("Weighted image",weightedsum)
sub = cv2.subtract(image1,image2)   #subtraction
cv2.imshow("Subtracted image",sub)
#Bitwise operations on images
dest_and = cv2.bitwise_and(image2,image1,mask=None)   #Bitwise And
cv2.imshow("Bitwise and" , dest_and)
dest_or = cv2.bitwise_or(image2,image1,mask=None)     #Bitwise Or
cv2.imshow("Bitwise or",dest_or)     
dest_xor = cv2.bitwise_xor(image1,image2)             #Bitwise xor
cv2.imshow("Bitwise xor",dest_xor)
dest_not1 = cv2.bitwise_not(image1,mask=None)         #NOT operation
dest_not2 = cv2.bitwise_not(image2,mask=None)
cv2.imshow("Image1",dest_not1)
cv2.imshow("Image2",dest_not2)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
