import urllib.request
import cv2
import numpy as np
import imutils
import requests
# import ssl
# context = ssl._create_unverified_context()
url = 'https://192.168.1.3:8080/shot.jpg'
response = requests.get(url, verify=False)
while True:
    imgPath = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgPath.read()), dtype=np.uint8)
    img = imutils.resize(img, width=450)
    cv2.imshow("CameraFeed", img)
    if ord('q') == cv2.waitKey(1):
        exit(0)