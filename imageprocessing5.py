#Find Co-ordinates of Contours using opencv python
import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX
image2 = cv2.imread('C:/Program Files/Python39/lena.png',cv2.IMREAD_COLOR)
image = cv2.imread('C:/Program Files/Python39/lena.png',cv2.IMREAD_GRAYSCALE)
_,threshold = cv2.threshold(image,110,255,cv2.THRESH_BINARY) #black and white img
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #detecting contours in image
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.009*cv2.arcLength(cnt,True),True)
    cv2.drawContours(image2,[approx],0,(0,0,255),5)
    n=approx.ravel()
    i=0
    for j in n:
        if(i%2==0):
            x=n[i]
            y=n[i+1]
            string=str(x)+""+str(y)
            if(i==0):
                cv2.putText(image2,"Arrow Tip",(x,y),font,0.5,(255,0,0))
            else:
                cv2.putText(image2,string,(x,y),font,0.5,(0,255,0))
    i=i+1
    cv2.imshow('image2',image2)
    if cv2.waitKey(0) & 0xff==ord('q'):
        cv2.destroyAllWindows()

