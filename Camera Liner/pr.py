
# import the opencv library
import cv2
import copy
import numpy as np
# define a video capture object
vid = cv2.VideoCapture(0)
ret, frame = vid.read()

shape=frame.shape
frm=np.zeros((shape[0],shape[1],3)).astype(np.uint8)
print(shape)
prep=-1
point=0
thickness=15
while(point<shape[1]):
	# Capture the video frame
	# by frame
	ret, frame = vid.read()
	frame=cv2.line(frame,(point,0),(point,shape[0]-1),thickness)
	for y in range(0,shape[0]):
		for i in range(prep,point):
			frm[y][i]=frame[y][i]
	for y in range(0,shape[0]):
		for i in range(0,point):
			frame[y][i]=frm[y][i]
	cv2.imshow('frame', frame)
	prep=point
	point+=7
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
