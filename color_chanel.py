import cv2 as cv
from cv2 import merge
img=cv.imread('Photos/about.jpg')
cv.imshow('img',img)

b,g,r=cv.split(img)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged image', merged)
cv.waitKey(0)