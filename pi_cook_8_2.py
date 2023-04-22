import cv2
from imutils.video import VideoStream
vs= VideoStream(scr=0).start() #the scr will search for the first camera, if there are more than one, then specify the camera that is goingt o be used. 
img = vs.read()
cv2.imshow('image',img)
cv2.waitKey(0)
