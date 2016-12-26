import cv2  
import numpy as np  
#import pdb  
#pdb.set_trace()#turn on the pdb prompt  
  
#read image  
img = cv2.imread('./car.jpg',cv2.IMREAD_COLOR)  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
cv2.imshow('origin',img);  
#SIFT  
detector = cv2.SIFT()  
keypoints = detector.detect(gray,None)  
img = cv2.drawKeypoints(gray,keypoints)  
#img = cv2.drawKeypoints(gray,keypoints,flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)  
cv2.imshow('test',img)
while(1):
	k=cv2.waitKey(5)&0xFF
	if k==27:
		break   
cv2.destroyAllWindows()  