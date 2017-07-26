import cv2
import os

for path in ["cam0", "cam1", "cam2"]:
	if not os.path.exists(path):
		os.makedirs(path)
cap0 = cv2.VideoCapture(0)
cap0.set(CV_CAP_PROP_FRAME_WIDTH,640);
cap0.set(CV_CAP_PROP_FRAME_HEIGHT,480);
cap1 = cv2.VideoCapture(1)
cap1.set(CV_CAP_PROP_FRAME_WIDTH,640);
cap1.set(CV_CAP_PROP_FRAME_HEIGHT,480);
cap2 = cv2.VideoCapture(2)
cap2.set(CV_CAP_PROP_FRAME_WIDTH,640);
cap2.set(CV_CAP_PROP_FRAME_HEIGHT,480);
#ret0, frame0 = cap0.read()
#cv2.imshow('frame', frame0)
count = 0

while 1:
	count+=1
	# do forever

	# capture the current frame
	ret0, frame0 = cap0.read()
	ret1, frame1 = cap1.read()
	ret2, frame2 = cap2.read()
	if frame0:
		cv2.imwrite("cam0/test"+str(count)+".jpg",frame0)
	else:
		print "camera 0 failed to capture"
	if frame1:
		cv2.imwrite("cam1/test"+str(count)+".jpg",frame1)
	else:
		print "camera 1 failed to capture"
	if frame2:
		cv2.imwrite("cam2/test"+str(count)+".jpg",frame2)
	else:
		print "camera 2 failed to capture"

	# handle events
	k = cv2.waitKey(10)

	if k == 0x1b: # ESC
	    print 'ESC pressed. Exiting ...'
	    break