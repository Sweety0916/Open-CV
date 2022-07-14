import cv2 as cv
import numpy as np

img =cv.imread('Photos/pic5.jpeg')
cv.imshow('Cat',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank, (img.shape[1]//2+45,img.shape[0]//2),100,25,-1)
cv.imshow('mask',mask)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked img',masked)
cv.waitKey(0)