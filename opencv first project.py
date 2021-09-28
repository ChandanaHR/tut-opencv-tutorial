#Extracting frames using opencv
#Taking a video as input and break the video into frame by frame and save those frames
import cv2
import numpy as np
#function to extract frames
def framecapture(path):
    #Path to video file
    vidObj = cv2.VideoCapture(path)
    count=0
    success=1
    while success:
        success,image=vidObj.read()
        cv2.imshow("frame%d.jpg" % count,image)
        count+=1

#Driver code
if __name__ == '__main__':
    framecapture('C:/Program Files/Python39/chandana.mp4')
