import cv2 as cv
#   reading images
img =cv.imread('Photos/about.jpg')
cv.imshow('Bg',img)
cv.waitKey(0)



#    reading videos

capture=cv.VideosCapture('Videos/about.mp4') #not having video now

while True:
    isTrue,frame=capture.read()
    cv.imshow('Videos',frame)
    
    if cv.waitKey(20)& 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

# run by python file_name.py