
import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('Blank',blank)
img =cv.imread('Photos/about.jpg')
cv.imshow('Cat',img)

# 1. paint the image a certain color
blank[:]=0,255,0
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)
# draw a rectangle


cv.rectangle(img,(0,0),(255,700),(0,255,0),thickness=-1)
cv.putText(img,'hello',(200,200),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv.imshow('Text',img)
cv.waitKey(0)

