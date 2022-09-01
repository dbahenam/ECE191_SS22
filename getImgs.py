import cv2
import time

cap = cv2.VideoCapture('Video/blueBuoy.mp4')
status,frame = cap.read()
num_images = 0

while True:
    cv2.imwrite ("Images/blueImgs/frame%d.jpg" % num_images, frame)
    status, frame = cap.read()
    print('Read a new frame: ', status)
    num_images += 1
