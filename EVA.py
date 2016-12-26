import numpy as np
import cv2
cap = cv2.VideoCapture('White nylon mask.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()#this funtion is in opencv3
#and createBackgroundSubtractorMOG is not used,we can just use createBackgroundSubtractorMOG2
while(1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	cv2.imshow('frame',fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
#ralph_young make it XXXXXX
