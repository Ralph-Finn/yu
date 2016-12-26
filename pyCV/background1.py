# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 00:26:52 2016

@author: Ralph
"""
#读取图像
'''
import cv2
#opencv 库是一个简单的库，可以使用cv.方法来进行调用。非常方便
im=cv2.imread('cat.png')
#显示图像
cv2.imshow('opencv', im)
cv2.waitKey()
'''
import cv2
import numpy as np
cap = cv2.VideoCapture("./car.mp4")
ret,frame = cap.read()
B0 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
I0 = B0
while(cap.isOpened()):
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',gray)
    k=cv2.waitKey(24)&0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()

