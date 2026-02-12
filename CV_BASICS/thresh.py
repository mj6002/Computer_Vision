import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('nature-6888085_960_720.jpg')

# Resize
img = cv.resize(img, (550,450), interpolation=cv.INTER_AREA)
cv.imshow('Resized', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 1)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)