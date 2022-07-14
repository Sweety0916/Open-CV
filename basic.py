import cv2 as cv
from cv2 import detail_FeatherBlender
from cv2 import resize
img =cv.imread('Photos/pic5.jpeg')
cv.imshow('Cat',img)


# converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_CONSTANT)
cv.imshow('blur',blur)



# edge cascade

canny=cv.Canny(img,125,174)
cv.imshow('canny',canny)

# dilating the image
dilated=cv.dilate(img,(3,3),iterations=1)
cv.imshow('dilating',dilated)


#eroding
erodedg=cv.erode(img,(3,3),iterations=3)
cv.imshow('eroding',erodedg)


#resized

resized=cv.resize(img,[150,120],interpolation=cv.INTER_AREA)
cv.imshow('resizeing',resized)

# rotation

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






