# import the opencv library
import cv2


# define a video capture object
vid1 = cv2.VideoCapture(2)
vid2 = cv2.VideoCapture(4)

while(True):
	
	# Capture the video frame
	# by frame
	ret, frame1 = vid1.read()
	ret, frame2 = vid2.read()

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


	# Display the resulting frame
	cv2.imshow('frame1', frame1)
	cv2.imshow('frame2', frame2)
	

# After the loop release the cap object
vid1.release()
vid2.release()

# Destroy all the windows
cv2.destroyAllWindows()
