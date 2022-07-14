from random import gauss
from statistics import median
import cv2 as cv
from cv2 import bilateralFilter
from flask import redirect
img=cv.imread('Photos/about.jpg')
cv.imshow('img',img)


# averaging

average=cv.blur(img,(7,7))
# increase blur (3,3 to (7,7))
cv.imshow('avegare blur', average)

#Gaussian blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian blur',gauss)

# median blur

median=cv.medianBlur(img,3)
cv.imshow('median blur',median)

# bilateral 
bilateral=cv.bilateralFilter(img, 10, 35,20)
cv.imshow('bilateral blur',bilateral)

cv.waitKey(0)
