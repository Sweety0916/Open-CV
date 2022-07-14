import cv2 as cv
import matplotlib.pyplot as plt


img =cv.imread('Photos/about.jpg')
cv.imshow('color_spaces',img)

plt.imshow(img)
plt.show()

#BGR TO Grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR TO HSV

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)

# BGR TO L*A+B

lab=cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

#BGR TO RGB

rgb=cv.cvtColor(img,cv.COLOR_RGB2BGR)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show()

#hsv to bgr
#lab to bgr
#gray to bgr
hsv_rgb=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('rgb',hsv_rgb)

cv.waitKey(0)