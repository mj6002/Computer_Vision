import numpy as np
import cv2 as cv

img = cv.imread('pat-whelen--9zbTfPFxoI-unsplash.jpg')

# Resize
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 65, img.shape[0]//2), 100, 255, -1)
cv.imshow('circle', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('wired shaped masked image', weird_shape)

masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Masked Image', masked)


cv.waitKey(0)