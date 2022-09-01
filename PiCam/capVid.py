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

