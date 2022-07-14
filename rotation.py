from turtle import width
import numpy as np
import cv2 as cv

img =cv.imread('Photos/pic5.jpeg')
# cv.imshow('Cat',img)

def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    
    if rotPoint is None:
        rotPoint=(width//2,height//2)
        
        rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
        dimension=(width,height)

    return cv.warpAffine(img,rotMat,dimension)
rotated= rotate(img,-45)
cv.imshow('rotate',rotated)

rotated_rotated=rotate(rotated,-45)
cv.imshow('rotate',rotated)

cv.waitKey(0)
