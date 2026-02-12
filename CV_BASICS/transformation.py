import numpy as np
import cv2 as cv

img = cv.imread('pat-whelen--9zbTfPFxoI-unsplash.jpg')

# Resize
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('rotated rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
'''
0 --> Vertical flip
1 --> Horizontal flip
-1 --> Vertical + Horizontal flip
'''
flip = cv.flip(img, 1)
cv.imshow('flipped', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)