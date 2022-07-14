from gettext import _TranslationsReader
import cv2 as cv
import numpy as np
img =cv.imread('Photos/pic5.jpeg')
cv.imshow('Cat',img)

#transformation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimension=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimension)

translated = translate(img,100,100)
cv.imshow('translate',translated)
# -x=left
# -y = up
# x=right
# y= down
cv.waitKey(0)