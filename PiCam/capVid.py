import depthai as dai
import cv2

pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)

xoutVideo.setStreamName("video")

# Properties
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setVideoSize(900, 700)
size = (900, 700)
xoutVideo.input.setBlocking(False)
xoutVideo.input.setQueueSize(1)

# Linking
camRgb.video.link(xoutVideo.input)

with dai.Device(pipeline) as device:

	video = device.getOutputQueue(name="video", maxSize=1, blocking=False)
	result = cv2.VideoWriter('Video/filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
	while True:
		videoIn = video.get()
		original = videoIn.getCvFrame()
		frame = cv2.resize(original, None, fx = 1, fy = 1, interpolation=cv2.INTER_AREA)
		result.write(frame)
		cv2.imshow('Input', frame)
		c = cv2.waitKey(1)
		
		if c == 27:
			break
			
	cv2.destroyAllWindows()
result.release()
        # Get resolutions.
        # frame_width = int(.get(3))
        # frame_height = int(video.get(4))

        #size = (frame_width, frame_height)

        # Below VideoWriter object will create
        # a frame of above defined The output
        # is stored in 'filename.avi' file.
        # result = cv2.VideoWriter('Video/aRecording.avi',
        #                         cv2.VideoWriter_fourcc(*'MJPG'),
        #                         10, size)

    # while (True):
    #     ret, frame = video.read()

    #     if ret == True:

    #         result.write(frame)
    #         cv2.imshow('Frame', frame)

    #         # Press S on keyboard
    #         # to stop the process
    #         if cv2.waitKey(1) & 0xFF == ord('s'):
    #             break

    #     # Break the loop
    #     else:
    #         break

    # # When everything done, release
    # # the video capture and video
    # # write objects
    # video.release()
    # result.release()

    # # Closes all the frames
    # cv2.destroyAllWindows()

    # print("The video was successfully saved")
