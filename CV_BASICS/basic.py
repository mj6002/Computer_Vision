import cv2 as cv

# reading images
img = cv.imread('pat-whelen--9zbTfPFxoI-unsplash.jpg')

cv.imshow('goku', img)


def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

# Converting to grayscale
gray = cv.cvtColor(resized_image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Bluring Image
blur = cv.GaussianBlur(resized_image, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dialating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dialated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7,), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)