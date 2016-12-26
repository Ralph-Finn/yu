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
cap=cv2.VideoCapture(0)
while(1):
    # 获取每一帧
    ret,frame=cap.read()
    # 䤛换到 HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #颜色转换函数均是在cvtColor这个函数中的。
    # 䕭定蓝色的侷值
    lower_blue=np.array([110,50,50])
    upper_blue=np.array([130,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    res=cv2.bitwise_and(frame,frame,mask=mask)
    # 显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)&0xFF
    if k==27:
        break
# 关侜窗口
cv2.destroyAllWindows()
 