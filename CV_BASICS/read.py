import cv2 as cv

# reading images
# img = cv.imread('c:/Users/Manan Jain/Pictures/WALLPAPERS/anime/781768.png')

# cv.imshow('goku', img)

# reading videos
capture = cv.VideoCapture('c:/Users/Manan Jain/Videos/Captures/OpeningManimExample 2023-01-14 13-54-14.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows( )

cv.waitKey(0) 