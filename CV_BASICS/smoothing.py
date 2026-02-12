import cv2 as cv

img = cv.imread('nature-6888085_960_720.jpg')

# Resize
img = cv.resize(img, (500,400), interpolation=cv.INTER_AREA)
cv.imshow('Resized', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('AVG blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)