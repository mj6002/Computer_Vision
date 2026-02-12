import numpy as np
import cv2 as cv

img = cv.imread('nature-6888085_960_720.jpg')

# Resize
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('Resized', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])



cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)