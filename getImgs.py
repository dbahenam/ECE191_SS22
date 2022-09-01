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

# If there is an error with reading certain frames throughout video...
# start_time = time.time()
# video_length = 27

# while int(time.time() - start_time) < video_length:

#     if status:
#         cv2.imwrite("Images/blueImgs/frame%d.jpg" % num_images, frame)
#     status,frame = cap.read()
#     print('Read a new frame: ', status)
#     num_images += 1